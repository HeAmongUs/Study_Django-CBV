from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import UserRegistrationForm, UserLoginForm
from apps.utils import DataMixin
from .models import Profile
from .utils import create_user_on_form
from ..news.utils import get_news_queryset


class RegisterUser(DataMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        create_user_on_form(form)
        # Перенаправление но созданный профиль
        return redirect(self.success_url)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(context_mixin.items()))


class LoginUser(DataMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(context_mixin.items()))


class ProfileView(DataMixin, DetailView):
    model = Profile
    slug_url_kwarg = "profile_slug"
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile'
    template_name = 'account/profile.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_context(title=context['profile'].user.username)
        context['news'] = get_news_queryset(author=context['profile'].user)
        print(context["profile"])
        return dict(list(context.items()) + list(context_mixin.items()))
