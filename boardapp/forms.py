from django.forms import ModelForm

from boardapp.models import Board


class BoardCreationForm(ModelForm):
    class Meta:
         model = Board
         fields = ['title', 'description']