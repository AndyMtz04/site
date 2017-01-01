from django.shortcuts import render
from .models import Post, Project, About


def index(request):
    return render(request, 'index.html')


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