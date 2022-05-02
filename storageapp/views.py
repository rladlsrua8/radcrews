import mimetypes
import os
import urllib

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.staticfiles import storage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, Http404

from storageapp.decorators import storage_ownership_required
from storageapp.forms import StorageCreationForm
from storageapp.models import Storage
from commentapp.forms import CommentCreationForm
from storagecommentapp.forms import StorageCommentCreationForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class StorageCreateView(UserPassesTestMixin, CreateView):
    model = Storage
    form_class = StorageCreationForm
    template_name = 'storageapp/create.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        temp_storage = form.save(commit=False)
        temp_storage.writer = self.request.user
        temp_storage.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('storageapp:detail', kwargs={'pk': self.object.pk})

class StorageDetailView(DetailView):
    model = Storage
    context_object_name = 'target_storage'
    template_name = 'storageapp/detail.html'


@method_decorator(storage_ownership_required, 'get')
@method_decorator(storage_ownership_required, 'post')
class StorageUpdateView(UpdateView):
    model = Storage
    context_object_name = 'target_storage'
    form_class = StorageCreationForm
    template_name = 'storageapp/update.html'

    def get_success_url(self):
        return reverse('storageapp:detail', kwargs={'pk': self.object.pk})

class StorageDetailView(DetailView, FormMixin):
    model = Storage
    form_class = StorageCommentCreationForm
    context_object_name = 'target_storage'
    template_name = 'storageapp/detail.html'

@method_decorator(storage_ownership_required, 'get')
@method_decorator(storage_ownership_required, 'post')
class StorageDeleteView(DeleteView):
    model = Storage
    context_object_name = 'target_storage'
    success_url = reverse_lazy('storageapp:list')
    template_name = 'storageapp/delete.html'

@method_decorator(login_required, 'get')
class StorageListView(UserPassesTestMixin, ListView):
    model = Storage
    context_object_name = 'storage_list'
    template_name = 'storageapp/list.html'
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-id"

    def test_func(self):
        return self.request.user.is_staff


def FileDownloadView(request, pk):
    storage = get_object_or_404(Storage, pk=pk)
    file_url = storage.upload.url[1:]

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_url)
            return response
        raise Http404