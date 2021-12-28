from django.forms import ModelForm

from storagecommentapp.models import StorageComment


class StorageCommentCreationForm(ModelForm):
    class Meta:
        model = StorageComment
        fields = ['content']
