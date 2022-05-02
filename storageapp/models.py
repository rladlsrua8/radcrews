import os
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Storage(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='storage', null=True)
    title = models.CharField(max_length=200, null=False)

    upload = models.FileField(upload_to='storage/%Y/%m/%d', null=False, blank=True)

    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)

    def get_filename(self):
        return os.path.basename(self.upload.name)