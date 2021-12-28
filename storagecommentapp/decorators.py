from django.http import HttpResponseForbidden

from storagecommentapp.models import StorageComment


def storagecomment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        storagecomment = StorageComment.objects.get(pk=kwargs['pk'])
        if not storagecomment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated