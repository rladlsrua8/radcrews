import mimetypes
import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView
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
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        post_list = Post.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_post_list = post_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__profile__nickname__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_post_list = post_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_post_list = post_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_post_list = post_list.filter(content__icontains=search_keyword)
                elif search_type == 'writer':
                    search_post_list = post_list.filter(writer__profile__nickname__icontains=search_keyword)

                return search_post_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type

        return context


class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
