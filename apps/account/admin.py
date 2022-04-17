from django.contrib import admin

from apps.account.models import Profile, Contact


@admin.register(Profile)
class AccountAdmin(admin.ModelAdmin):
    fields = ('user', 'slug', 'date_of_birth', )
    list_display = ('user', 'slug', 'date_of_birth', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('user_from', 'user_to', 'created')
    list_display = ('user_from', 'user_to', 'created')