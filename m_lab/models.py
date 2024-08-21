from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}




class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    preview_img = models.ImageField(verbose_name='превью', **NULLABLE)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
