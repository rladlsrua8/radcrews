from django.forms import ModelForm
from django import forms

from storageapp.models import Storage


class StorageCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto; text-align: left;'}))

    class Meta:
        model = Storage
        fields = ['title', 'upload', 'content']