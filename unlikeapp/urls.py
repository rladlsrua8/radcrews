from django.urls import path

from unlikeapp.views import UnlikeArticleView

app_name = 'unlikeapp'

urlpatterns = [
    path('article/unlike/<int:pk>', UnlikeArticleView.as_view(), name='article_unlike'),
]