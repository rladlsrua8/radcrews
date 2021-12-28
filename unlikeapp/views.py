from django.contrib import messages
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from unlikeapp.models import UnlikeRecord


@method_decorator(login_required, 'get')
class UnlikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        if UnlikeRecord.objects.filter(user=user, article=article).exists():
            messages.add_message(self.request, messages.ERROR, '싫어요는 한번만 가능합니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            UnlikeRecord(user=user, article=article).save()

        article.unlike += 1
        article.save()

        messages.add_message(self.request, messages.SUCCESS, '싫어요가 반영되었습니다.')

        return super(UnlikeArticleView, self).get(self.request, *args, **kwargs)