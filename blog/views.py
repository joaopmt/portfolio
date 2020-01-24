from django.shortcuts import render, get_object_or_404

from .models import Blog

def blogs_home(request):
    blogs = Blog.objects
    return render(request, 'blog/blogs_home.html', {'blogs': blogs, 'teste': [1,2,3] })

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detail_blog})