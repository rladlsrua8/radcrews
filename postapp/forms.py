import taggit.views
from django.forms import ModelForm
from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget
from postapp.models import Post
from taggit.forms import *

categories =(
    ('구인구직', '구인구직'),
    ('경제', '경제'),
    ('정치', '정치'),
    ('기타', '기타'),
)

class PostCreationForm(ModelForm):
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '게시글 제목',
            }
        ),
        required=True,
    )

    content = SummernoteTextField()

    field_order = [
        'title',
        'tags',
        'content',
    ]


    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tags',
        ]
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {
                'width':'100%',
                'height':'400px',
                'attachment_filesize_limit': 10 * 1024 * 1024,
            }}),
            'tags': forms.Select(choices=categories)
        }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        content =  cleaned_data.get('content', '')

        if title == '':
            self.add_error('title', '글제목을 입력하세요')
        elif content == '':
            self.add_error('content', '글내용을 입력하세요')
        else:
            self.title = title
            self.content = content
