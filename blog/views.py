from django.shortcuts import render

from .models import Blog

def blogs_home(request):
    blogs = Blog.objects
    return render(request, 'blog/blogs_home.html', {'blogs': blogs, 'teste': [1,2,3] })
