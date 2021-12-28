import mimetypes
import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, Http404

from postapp.decorators import post_ownership_required
from postapp.forms import PostCreationForm
from postapp.models import Post
from commentapp.forms import CommentCreationForm

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class PostCreateView(UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'postapp/create.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        temp_post = form.save(commit=False)
        temp_post.writer = self.request.user
        temp_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.pk})

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'target_post'
    template_name = 'postapp/detail.html'


@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'target_post'
    form_class = PostCreationForm
    template_name = 'postapp/update.html'

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.pk})

class PostDetailView(DetailView, FormMixin):
    model = Post
    form_class = CommentCreationForm
    context_object_name = 'target_post'
    template_name = 'postapp/detail.html'

@method_decorator(post_ownership_required, 'get')
@method_decorator(post_ownership_required, 'post')
class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'target_post'
    success_url = reverse_lazy('postapp:list')
    template_name = 'postapp/delete.html'

@method_decorator(login_required, 'get')
class PostListView(UserPassesTestMixin, ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'postapp/list.html'
    ordering = "-id"
    paginate_by = 10
    paginate_orphans = 5

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['jobs_boards'] = Post.objects.filter(board_name='Jobs')
        context['posts_boards'] = Post.objects.filter(board_name='Posts')
        return context


