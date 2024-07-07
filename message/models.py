from django.db import models

from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема", )
    message = models.TextField(verbose_name="Сообщение")
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

