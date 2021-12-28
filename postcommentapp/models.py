from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from postapp.models import Post


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='postcomment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='postcomment')

    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='postcomment/', null=True, blank=True)