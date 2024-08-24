from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}




class Post(models.Model):

    blog_title = models.CharField(max_length=200)
    blog_subtitle = models.CharField(max_length=200)
    blog_text = models.TextField(**NULLABLE)

    about_text = models.TextField(**NULLABLE)

    def formatted_blog_text(self):
        return self.blog_text.replace("\n", "<br>")

    formatted_blog_text.allow_tags = True

    
    def __str__(self):
        return self.blog_title
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
