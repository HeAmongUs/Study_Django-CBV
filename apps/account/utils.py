from django.contrib.auth.models import User

from apps.account.models import Profile


def get_user_queryset(**kwargs):
    return User.objects.filter(**kwargs)


def create_user_on_form(form):
    form.save()
    user = get_user_queryset(username=form.data['username'])[0]
    profile = Profile(user=user)
    profile.set_default_profile_slug_id()
    profile.save()



