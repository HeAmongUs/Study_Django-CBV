from django.urls import path

from .views import NewsList, NewsCreate, NewsDetail, NewsByTagList, CommentCreate

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/tag/<slug:tag_slug>/', NewsByTagList.as_view(), name='news_by_tag'),
    path('news/comment/', CommentCreate.as_view(), name='comment_create'),
    path('news/<slug:news_slug>/', NewsDetail.as_view(), name='news_detail'),
]