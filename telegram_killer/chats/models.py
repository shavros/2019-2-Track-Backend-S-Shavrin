from django.db import models

from django.db import models

# Create your models here.


class Chat(models.Model):
    is_group_chat = models.BooleanField(default=False, verbose_name='Групповой чат')
    topic = models.CharField(max_length=16, verbose_name='Тема')
    last_message = models.CharField(max_length=32, default='null', verbose_name='Последнее сообщение')


class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, verbose_name='id чата')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='id пользователя')
    content = models.TextField(verbose_name='Содержание сообщения')
    added_at = models.DateTimeField(null=False, auto_now=True, verbose_name='Дата и время отправкивки')


class Attachment(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, verbose_name='id чата')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='id ользователя')
    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='id сообщения')
    type = models.CharField(max_length=16, verbose_name='Тип содержимого')
    url = models.URLField(verbose_name='Ссылка на вложение')
