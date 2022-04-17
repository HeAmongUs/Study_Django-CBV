from .news.utils import get_tags, get_news_by_tag

MENU = [
    {'title': 'News', 'url_name': 'news'},
    {'title': 'Create news', 'url_name': 'news_create'},

]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = MENU
        if 'tags' in context:
            context['tags'] = get_tags()

            for tag in context['tags']:
                tag.count_of_news = len(get_news_by_tag(tag))

        return context
