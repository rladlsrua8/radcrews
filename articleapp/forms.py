from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto; text-align: left;'}))
    project = forms.ModelChoiceField(Project.objects.all(), label="Specialty", required=False, empty_label="Selected Specialty")

    class Meta:
        model = Article
        fields = ['title', 'project', 'image', 'image2', 'image3', 'image4', 'image5','content']
