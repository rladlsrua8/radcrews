from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm




@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(UserPassesTestMixin, CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'
    permission_denied_message = "인증 후 이용 가능합니다"

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'

@method_decorator(login_required, 'get')
class ArticleListView(UserPassesTestMixin, ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        article_list = Article.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_article_list = article_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__profile__nickname__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_article_list = article_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_article_list = article_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_article_list = article_list.filter(content__icontains=search_keyword)
                elif search_type == 'writer':
                    search_article_list = article_list.filter(writer__profile__nickname__icontains=search_keyword)

                return search_article_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return article_list

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
