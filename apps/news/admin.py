from django.contrib import admin

from .models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_create',)
    fields = ('title', 'slug', 'text', 'is_published', 'tags', 'author', )
    list_display = ('title', 'get_tags_name', 'author', 'datetime_create')
    prepopulated_fields = {'slug': ('tags', 'title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'author', 'created', 'text')
    list_filter = ('author', 'created')
    search_fields = ('news', 'text', 'author')
    prepopulated_fields = {'slug': ('news', 'author','text',)}