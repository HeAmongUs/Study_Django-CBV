from taggit.models import Tag

from .models import News


def get_news_queryset(**kwargs):
    return News.objects.filter(**kwargs)


def get_tags(**kwargs):
    return Tag.objects.filter(**kwargs)


def create_comment_on_form(form, author):
    new_comment = form.save(commit=False)
    news = get_news_queryset(slug=form.data['news_slug'])[0]
    new_comment.author = author
    new_comment.news = news
    new_comment.save()


def get_news_comments(news):
    return news.comments.all()


def get_news_by_tag(tag):
    return get_news_queryset(tags__in=[tag], is_published=True)
