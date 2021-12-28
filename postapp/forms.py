from django.forms import ModelForm
from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

from postapp.models import Post


class PostCreationForm(ModelForm):
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '게시글 제목'
            }
        ),
        required=True,
    )

    content = SummernoteTextField()

    options = (
        ('Posts', '기타'),
        ('Jobs', '구인구직')
    )

    board_name = forms.ChoiceField(
        label='게시판 선택',
        widget=forms.Select(),
        choices=options
    )

    field_order = [
        'title',
        'board_name',
        'content'
    ]


    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'board_name'
        ]
        widgets = {
            'content' : SummernoteWidget()
        }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        content =  cleaned_data.get('content', '')
        board_name = cleaned_data.get('board_name', 'Posts')

        if title == '':
            self.add_error('title', '글제목을 입력하세요')
        elif content == '':
            self.add_error('content', '글내용을 입력하세요')
        else:
            self.title=title
            self.content=content
            self.board_name=board_name
