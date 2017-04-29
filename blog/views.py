from django.shortcuts import render
from .models import Project, About, FrontPage, FrontPageProject


def index(request):
    front = FrontPage.objects.first()
    projects = FrontPageProject.objects.all()
    return render(request, 'index.html', {'projects': projects, 'front': front})


#def blog(request):
#    active = 'blog'
#    posts = Post.objects.all()
#    return render(request, 'blog.html', {'posts': posts, 'active': active})


def projects(request):
    active = 'projects'
    posts = Project.objects.all().order_by("created_date")
    return render(request, 'projects.html', {'posts': posts, 'active': active})


def about(request):
    active = 'about'
    posts = About.objects.all()
    return render(request, 'about.html', {'posts': posts, 'active': active})