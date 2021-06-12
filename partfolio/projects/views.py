from django.shortcuts import render
from .models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {'projects': projects}
    return render(request, 'project_detail.html', context)
