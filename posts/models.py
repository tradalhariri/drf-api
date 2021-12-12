from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
    
