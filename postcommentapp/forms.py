from django.forms import ModelForm

from postcommentapp.models import PostComment


class PostCommentCreationForm(ModelForm):
    class Meta:
        model = PostComment
        fields = ['image', 'content']
