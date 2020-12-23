from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ex1')
    image = models.ImageField(upload_to='posts')
    created_add = models.DateTimeField(auto_now_add=True)
    update_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} --> {self.title}"