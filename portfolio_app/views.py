import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogPost
from django.conf import settings
def home_view(request):
    return render(request, 'home.html')

def projects_view(request):
    # Fetch GitHub repos
    github_url = "https://api.github.com/users/fahad14al/repos"
    headers = {}
    if hasattr(settings, 'GITHUB_TOKEN') and settings.GITHUB_TOKEN:
        headers['Authorization'] = f"token {settings.GITHUB_TOKEN}"
        
    try:
        response = requests.get(github_url, headers=headers, timeout=5)
        response.raise_for_status()
        repos = response.json()
        
        # Sort by updated_at descending
        repos.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
    except Exception as e:
        print(f"Error fetching GitHub repos: {e}")
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
    return render(request, "contact.html")

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
