from django.db import models

from email_massages.models import EmailMessage

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Logi(models.Model):
    """
    Модель для хранения информации о попытках рассылок
    """
    SUCCESS = 'Успешно'
    FAIL = 'Неуспешно'
    STATUS_VARIANTS = [
        (SUCCESS, 'Успешно'),
        (FAIL, 'Неуспешно'),
    ]

    time = models.DateTimeField(
        verbose_name="Дата и время попытки отправки", auto_now_add=True
    )
    status = models.CharField(max_length=50, choices=STATUS_VARIANTS, verbose_name='Cтатус рассылки')
    server_response = models.CharField(
        max_length=150, verbose_name="Ответ сервера почтового сервиса", **NULLABLE
    )
    email_message = models.ForeignKey(EmailMessage, on_delete=models.CASCADE, verbose_name="Рассылка")

    def __str__(self):
        return f"{self.mailing} {self.time} {self.status} {self.server_response}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
