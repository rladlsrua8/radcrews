from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from postapp.models import Post
from boardapp.forms import BoardCreationForm
from boardapp.models import Board
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class BoardCreateView(UserPassesTestMixin, CreateView):
    model = Board
    form_class = BoardCreationForm
    template_name = 'boardapp/create.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse('boardapp:detail', kwargs={'pk': self.object.pk})

class BoardDetailView(DetailView, MultipleObjectMixin):
    model = Board
    context_object_name = 'target_board'
    template_name = 'boardapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(board=self.get_object())
        return super(BoardDetailView, self).get_context_data(object_list=object_list,
                                                               **kwargs)

@method_decorator(login_required, 'get')
class BoardListView(UserPassesTestMixin, ListView):
    model = Board
    context_object_name = 'board_list'
    template_name = 'boardapp/list.html'
    paginate_by = 25

    def test_func(self):
        return self.request.user.is_staff


class BoardDeleteView(DeleteView):
    model = Board
    context_object_name = 'target_board'
    success_url = reverse_lazy('postapp:list')
    template_name = 'boardapp/delete.html'

