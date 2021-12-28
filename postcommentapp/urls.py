from django.urls import path

from postcommentapp.views import PostCommentCreateView, PostCommentDeleteView

app_name = 'postcommentapp'

urlpatterns = [
    path('create/', PostCommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', PostCommentDeleteView.as_view(), name='delete'),
]
