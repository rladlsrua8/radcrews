from django.http import HttpResponseForbidden

from postcommentapp.models import PostComment


def postcomment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        postcomment = PostComment.objects.get(pk=kwargs['pk'])
        if not postcomment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated