from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    slug = models.SlugField(blank=True, unique=True, verbose_name="Адрес профиля")

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_slug': self.slug})

    def set_default_profile_slug_id(self):
        try:
            self.slug = slugify(self.user.username)
        except:
            ValueError("Невозможно преобразовать имя пользователя в slug")


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


# Динамическое добавление поля following в модель User
User.add_to_class('following', models.ManyToManyField('self', through=Contact,
                                                      related_name='followers', symmetrical=False))
