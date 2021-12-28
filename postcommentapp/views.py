from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from postapp.models import Post
from postcommentapp.decorators import postcomment_ownership_required
from postcommentapp.forms import PostCommentCreationForm
from postcommentapp.models import PostComment


class PostCommentCreateView(CreateView):
    model = PostComment
    form_class = PostCommentCreationForm
    template_name = 'postcommentapp/create.html'

    def form_valid(self, form):
        temp_postcomment = form.save(commit=False)
        temp_postcomment.post = Post.objects.get(pk=self.request.POST['post_pk'])
        temp_postcomment.writer = self.request.user
        temp_postcomment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.post.pk})


@method_decorator(postcomment_ownership_required, 'get')
@method_decorator(postcomment_ownership_required, 'post')
class PostCommentDeleteView(DeleteView):
    model = PostComment
    context_object_name = 'target_postcomment'
    template_name = 'postcommentapp/delete.html'

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.post.pk})
