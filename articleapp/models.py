from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=False)

    image = models.ImageField(upload_to='article/%Y/%m/%d', null=False)
    image2 = models.ImageField(upload_to='article/%Y/%m/%d', null=True, blank=True)
    image3 = models.ImageField(upload_to='article/%Y/%m/%d', null=True, blank=True)
    image4 = models.ImageField(upload_to='article/%Y/%m/%d', null=True, blank=True)
    image5 = models.ImageField(upload_to='article/%Y/%m/%d', null=True, blank=True)

    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
