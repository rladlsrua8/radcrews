from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from storageapp.models import Storage


class StorageComment(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True, related_name='storagecomment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='storagecomment')

    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='storagecomment/', null=True, blank=True)