from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django import forms
from .forms import NewAccountForm





# def blog_hello(request):
#     return HttpResponse('hello')


# def post_list(request):
#     # post = Post.objects.filter(status='published')
#     posts = Post.published.all()
#     paginator = Paginator(posts,1)
#     page = request.GET.get('page')
#
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     return render(request, 'blog/post/list.html', {'posts':posts, 'page':page})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blog/post/list.html'


def details(request, title, year, month):
    post = get_object_or_404(Post, status='published', slug=title, publish__year=year, publish__month=month)
    return render(request, 'blog/post/details.html', {'post' : post})

# Create New Form (and Send To Add a Name In Admin/New Accounts)
def new_account(request):
    if request.method == 'POST':
        form = NewAccountForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewAccountForm()
    return render(request, 'blog/forms/new_account.html', {'form' : form})