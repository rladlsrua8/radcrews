from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='post', null=True)
    title = models.CharField(max_length=200, null=False)

    tags = TaggableManager(blank=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    hits = models.PositiveIntegerField(default=0)

    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('postapp:detail', args=[self.id])

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'

