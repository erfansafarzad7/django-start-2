from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post



# def blog_hello(request):
#     return HttpResponse('hello')


def post_list(request):
    # post = Post.objects.filter(status='published')
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts':posts})


def details(request, title, year, month):
    post = get_object_or_404(Post, status='published', slug=title, publish__year=year, publish__month=month)
    return render(request, 'blog/post/details.html', {'post':post})