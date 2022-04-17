from django import forms
from .models import News, Comment


class CreateNewsFrom(forms.ModelForm):
    class Meta:
        model = News
        readonly_fields = ['datetime_create', ]
        fields = ('title', 'slug', 'text', 'is_published', 'tags', 'author', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'news-from__input__text'}),
            'slug': forms.TextInput(attrs={'class': 'news-from__input__text'}),
            'text': forms.Textarea(attrs={'class': 'news-from__input__text'}),
        }


class CreateCommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        readonly_fields = ['created', 'news', 'author']
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'news-comment-from__input__text'}),
        }


