from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=False, default='default.jpg')
    nickname = models.CharField(max_length=25, unique=True, null=True)

    useremail = models.EmailField(max_length=128, null=True)
