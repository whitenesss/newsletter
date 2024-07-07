from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='Email', unique=True)
    name = models.CharField(max_length=150, verbose_name='ФИО', help_text='введите ФИО')
    comments = models.TextField(verbose_name='Comments', **NULLABLE, help_text='коментарии')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients', **NULLABLE)

    def __str__(self):
        return f'{self.email}: {self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
