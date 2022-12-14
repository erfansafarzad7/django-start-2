from django.contrib import admin
from .models import Post, NewAccount

# admin.site.register(Post)

# Create Post Table In Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'publish', 'status')
    list_filter = ('status', 'author', 'publish', 'create')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    # row_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)
    list_editable = ('status',)
    list_display_links = ('title', 'slug',)

# Create AccountName Table In Admin
@admin.register(NewAccount)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name',)