from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('blog', views.blog_hello, name='blog'),
    path('list/', views.post_list, name='list'),
    path('details/<slug:title>/<int:year>/<int:month>/', views.details, name='details'),
]
