from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    name = models.CharField(max_length=16)
    avatar = models.ImageField()
    nick = models.CharField(max_length=16)


class Member(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    chat = models.ForeignKey('chats.Chat', on_delete=models.CASCADE)
    new_messages = models.TextField()
    last_read_message = models.ForeignKey('chats.Message', on_delete=models.CASCADE)

