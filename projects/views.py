from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projectsPage(request):
    return render(request, 'projects/projects.html')
