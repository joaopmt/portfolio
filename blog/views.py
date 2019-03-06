from django.shortcuts import render

from . import models

def blogs_home(request):
    blogs = models.Blog.objects
    return render(request, 'blog/blogs_home.html', {'blogs': blogs, 'teste': [1,2,3] })
