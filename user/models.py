from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers import CustomUserManager

NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractUser):
    """
    Модель, описывающая пользователя сервиса рассылок.
    Наследуется от AbstractUser.
    """
    objects = CustomUserManager()

    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    email_verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', default='users/default.png')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    country = models.CharField(max_length=100, verbose_name='Страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'