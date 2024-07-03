from django.db import models

from clients.models import Client
from message.models import Message
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class EmailMessage(models.Model):
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = "Создана"
    STARTED = "Запущена"
    COMPLETED = "Завершена"

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(**NULLABLE, verbose_name="Описание", help_text="не обязательное поле")
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default=CREATED, verbose_name="Статус")
    periodicity = models.CharField(
        max_length=150,
        choices=PERIODICITY_CHOICES,
        default=DAILY,
        verbose_name="Периодичность",
    )
    start_date = models.DateTimeField(
        verbose_name="Дата начала",
        **NULLABLE,
        help_text="(формат 04.07.2024) не обязательное поле",
    )
    end_date = models.DateTimeField(verbose_name='Дата окончания', **NULLABLE, help_text='не обязательное поле')
    next_send_time = models.DateTimeField(verbose_name='Время следующей отправки',
                                          help_text="(формат 04.07.2024 00:00:00) обязательное поле", **NULLABLE)
    clients = models.ManyToManyField(Client, related_name='mailing', verbose_name='Клиенты для рассылки')
    message = models.ForeignKey(Message, verbose_name='Cообщение', on_delete=models.CASCADE, **NULLABLE)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f"{self.name}, статус: {self.status}"

    def save(self, *args, **kwargs):
        if not self.next_send_time:
            self.next_send_time = self.start_date
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("name",)
        permissions = [
            ('deactivate_emailmessage', 'Can deactivate mailing'),
            ('view_all_emailmessage', 'Can view all mailings'),
        ]
