from django.urls import path

from storagecommentapp.views import StorageCommentCreateView, StorageCommentDeleteView

app_name = 'storagecommentapp'

urlpatterns = [
    path('create/', StorageCommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', StorageCommentDeleteView.as_view(), name='delete'),
]
