from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'