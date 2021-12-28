from django.urls import path

from postapp.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from storageapp import views

app_name = 'postapp'

urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/', views.FileDownloadView, name='download'),
    ]