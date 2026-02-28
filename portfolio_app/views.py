import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import BlogPost
from django.core.mail import send_mail
from django.conf import settings
def home_view(request):
    return render(request, 'home.html')

def projects_view(request):
    # Fetch GitHub repos
    github_url = "https://api.github.com/users/fahad14al/repos"
    try:
        response = requests.get(github_url, timeout=5)
        response.raise_for_status()
        repos = response.json()
        
        # Sort by updated_at descending
        repos.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
    except Exception as e:
        repos = []
        messages.error(request, "Could not load projects from GitHub at this time.")

    context = {
        'repos': repos
    }
    return render(request, 'projects.html', context)

def blog_view(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, 'blog.html', {'posts': posts})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send an email notification
            subject = f"New Contact Portfolio Message from {contact.name}"
            email_message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"
            try:
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Log or handle the exception if needed
                print(f"Error sending email: {e}")

            messages.success(request, "Your message has been sent successfully! I will get back to you soon.")
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
