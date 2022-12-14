from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# class PostManager(models.Manager):
#     def year_filter(self, year):
#         return self.filter(publish__year= year)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# Create Fields For Post
class Post(models.Model):
    STATUS_CHOICES = (
        ('drafed', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post', default='author')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # objects=PostManager()
    objects = models.Manager()
    published = PublishedManager()

    def uniq_url(self):
        return reverse('blog:details', args=[self.slug, self.publish.year, self.publish.month])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

# Create Fields For NewName
class NewAccount(models.Model):
    name = models.CharField(max_length=20)