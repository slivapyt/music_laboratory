from django.contrib import admin
from m_lab.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('blog_title',)
    
