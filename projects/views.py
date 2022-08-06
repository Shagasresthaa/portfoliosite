import os
from django.shortcuts import render
from projects.models import projectsList

# Create your views here.

def projectsPage(request):

    projects = projectsList.objects.all()
    #https://site-media-storage-django-server017-testing.s3.ap-south-1.amazonaws.com/html_files/test.html

    bucket_name = os.environ.get('AWS_DJANGO_BUCKET_NAME')
    location = os.environ.get('AWS_DJANGO_LOCATION')
        
    #url = "https://%s.s3.%s.amazonaws.com/%s" % (bucket_name, location, object_name)

    lst = list(projects)
    for i in lst:
        url = "https://%s.s3.%s.amazonaws.com/%s" % (bucket_name, location, i.html_files)
        i.html_files = url

    return render(request, 'projects/projects.html', {'projects': lst})
