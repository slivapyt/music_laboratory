from django.contrib import admin
from m_lab.models import Photo, Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('blog_title',)
    

@admin.register(Photo)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
