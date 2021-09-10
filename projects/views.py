from django.shortcuts import render
from projects.models import projectsList

# Create your views here.

def projectsPage(request):

    projects = projectsList.objects.all()

    return render(request, 'projects/projects.html', {'projects': list(projects)})
