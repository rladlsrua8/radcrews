from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from storageapp.models import Storage
from storagecommentapp.decorators import storagecomment_ownership_required
from storagecommentapp.forms import StorageCommentCreationForm
from storagecommentapp.models import StorageComment


class StorageCommentCreateView(CreateView):
    model = StorageComment
    form_class = StorageCommentCreationForm
    template_name = 'storagecommentapp/create.html'

    def form_valid(self, form):
        temp_storagecomment = form.save(commit=False)
        temp_storagecomment.storage = Storage.objects.get(pk=self.request.POST['storage_pk'])
        temp_storagecomment.writer = self.request.user
        temp_storagecomment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('storageapp:detail', kwargs={'pk': self.object.storage.pk})


@method_decorator(storagecomment_ownership_required, 'get')
@method_decorator(storagecomment_ownership_required, 'post')
class StorageCommentDeleteView(DeleteView):
    model = StorageComment
    context_object_name = 'target_storagecomment'
    template_name = 'storagecommentapp/delete.html'

    def get_success_url(self):
        return reverse('storageapp:detail', kwargs={'pk': self.object.storage.pk})
