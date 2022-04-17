from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from taggit.models import Tag

from apps.utils import DataMixin
from .forms import CreateNewsFrom, CreateCommentFrom
from .models import News
from .utils import get_news_queryset, get_news_comments, create_comment_on_form, get_news_by_tag


class NewsList(DataMixin, ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title='News', tags=True)
        context['count'] = len(context['news'])
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_queryset(self):
        return get_news_queryset(is_published=True)


class NewsDetail(LoginRequiredMixin, DataMixin, DetailView):
    login_url = 'login'
    model = News
    slug_url_kwarg = 'news_slug'
    context_object_name = 'news'
    template_name = 'news/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title=context['news'].title)
        context['comments'] = get_news_comments(context['news'])
        context['form'] = CreateCommentFrom
        return dict(list(context.items()) + list(context_mixin.items()))


class NewsByTagList(DataMixin, ListView):
    model = News
    slug_url_kwarg = 'tag_slug'
    context_object_name = 'news'
    template_name = 'news/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title=f'News by tag #{self.kwargs["tag_slug"]}', tags=True)
        context['count'] = len(context['news'])
        return dict(list(context.items()) + list(context_mixin.items()))

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return get_news_by_tag(tag)


class NewsCreate(DataMixin, CreateView):
    form_class = CreateNewsFrom
    template_name = 'news/create.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title='Добавить новость')
        return dict(list(context.items()) + list(context_mixin.items()))


class CommentCreate(LoginRequiredMixin, CreateView):
    form_class = CreateCommentFrom
    login_url = 'login'

    def form_valid(self, form):
        create_comment_on_form(form, self.request.user)
        # Перенаправление по адресу созданной новости
        return redirect(get_news_queryset(slug=form.data['news_slug'])[0].get_absolute_url())


