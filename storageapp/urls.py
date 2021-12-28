from django.urls import path
from django.views.generic import TemplateView

from storageapp import views
from storageapp.views import StorageCreateView, StorageDetailView, StorageUpdateView, StorageDeleteView, \
    StorageListView, FileDownloadView

app_name = 'storageapp'

urlpatterns = [
    path('list/', StorageListView.as_view(), name='list'),
    path('create/', StorageCreateView.as_view(), name='create'),
    path('detail/<int:pk>', StorageDetailView.as_view(), name='detail'),
    path('update/<int:pk>', StorageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', StorageDeleteView.as_view(), name='delete'),
    path('storage/<int:pk>/', views.FileDownloadView, name='download'),
    ]