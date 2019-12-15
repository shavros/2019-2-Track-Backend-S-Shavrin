from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    name = models.CharField(max_length=16, verbose_name='Имя пользователя')
    avatar = models.ImageField(verbose_name='Аватрака пользователя')
    nick = models.CharField(max_length=16, verbose_name='Никнейм пользователя')


class Member(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='id пользователя')
    chat = models.ForeignKey('chats.Chat', on_delete=models.CASCADE, verbose_name='id чата')
    new_messages = models.TextField(verbose_name='Новые сообщения')
    last_read_message = models.ForeignKey('chats.Message', on_delete=models.CASCADE, verbose_name='Последнее прочитанное сообщение')

