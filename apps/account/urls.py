from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegisterUser, LoginUser, ProfileView


urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<slug:profile_slug>/', ProfileView.as_view(), name='profile'),

]
