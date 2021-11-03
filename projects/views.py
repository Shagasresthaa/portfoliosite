from django.shortcuts import render
from projects.models import projectsList

# Create your views here.

def projectsPage(request):

    projects = projectsList.objects.all()
    useMobile = False
    if(request.user_agent.is_mobile or request.user_agent.is_tablet):
        useMobile = True
        
    #print(request.user_agent.is_mobile)

    return render(request, 'projects/projects.html', {'projects': list(projects), 'useMobile':useMobile})
