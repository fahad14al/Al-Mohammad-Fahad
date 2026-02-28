from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('projects/', views.projects_view, name='projects'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
]
