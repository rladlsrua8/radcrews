from django.http import HttpResponseForbidden

from storageapp.models import Storage


def storage_ownership_required(func):
    def decorated(request, *args, **kwargs):
        storage = Storage.objects.get(pk=kwargs['pk'])
        if not storage.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated