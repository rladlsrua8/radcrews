from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class UnlikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='unlike_record')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='unlike_record')

    class Meta:
        unique_together = ('user', 'article')
