from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('blog', views.blog_hello, name='blog'),
    # path('list/', views.post_list, name='list'),
    path('list/', views.PostListView.as_view(), name='list'),
    path('form/', views.new_account, name='form'),
    path('details/<slug:title>/<int:year>/<int:month>/', views.details, name='details'),
]
