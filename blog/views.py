from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blogPage(request):
    return render(request, 'blog/blog.html')
