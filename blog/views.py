import os
from django.shortcuts import render
from blog.models import blogsList

# Create your views here.

def blogPage(request):

    blogPosts = blogsList.objects.all()
    
    bucket_name = os.environ.get('AWS_DJANGO_BUCKET_NAME')
    location = os.environ.get('AWS_DJANGO_LOCATION')

    lst = list(blogPosts)
    for i in lst:
        url = "https://%s.s3.%s.amazonaws.com/%s" % (bucket_name, location, i.html_blog_post)
        i.html_blog_post = url

    return render(request, 'blog/blog.html', {"blogPosts": lst})
