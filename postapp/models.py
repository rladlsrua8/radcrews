import os
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='post', null=True)
    title = models.CharField(max_length=200, null=False)

    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    hits = models.PositiveIntegerField(default=0)
    board_name = models.CharField(max_length=32, default='Posts')

    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'

    def get_filename(self):
        return os.path.basename(self.upload.name)
