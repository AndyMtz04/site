from django.shortcuts import render, get_object_or_404
from .models import Project, About, FrontPage


def index(request):
    active = "AndyMtz"
    front = FrontPage.objects.first()
    projects = Project.objects.all().order_by("-created_date")[:3]
    return render(request, 'index.html', {'projects': projects, 'front': front, 'active': active})


#def blog(request):
#    active = 'blog'
#    posts = Post.objects.all()
#    return render(request, 'blog.html', {'posts': posts, 'active': active})


def projects(request):
    active = 'Projects'
    posts = Project.objects.all().order_by("-created_date")
    return render(request, 'projects.html', {'posts': posts, 'active': active})


def about(request):
    active = 'About'
    posts = About.objects.all()
    return render(request, 'about.html', {'posts': posts, 'active': active})


#def project(request, pk):
#    project = get_object_or_404(Project, pk=pk)
#    return render(request, 'project.html', {'project': project})