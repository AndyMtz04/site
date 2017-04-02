from django.shortcuts import render
from .models import Post, Project, About, FrontPage


def index(request):
    front = FrontPage.objects.first()
    projects = Project.objects.all()[:3]
    return render(request, 'index.html', {'projects': projects, 'front': front})


def blog(request):
    active = 'blog'
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'active': active})


def projects(request):
    active = 'projects'
    posts = Project.objects.all()
    return render(request, 'projects.html', {'posts': posts, 'active': active})


def about(request):
    active = 'about'
    posts = About.objects.all()
    return render(request, 'about.html', {'posts': posts, 'active': active})