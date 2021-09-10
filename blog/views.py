from django.shortcuts import render
from blog.models import blogsList

# Create your views here.

def blogPage(request):

    blogPosts = blogsList.objects.all()

    return render(request, 'blog/blog.html', {"blogPosts": blogPosts})
