import logging
import smtplib
from datetime import datetime, timedelta
import pytz
from django.core.mail import send_mail
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand


from email_massages.models import EmailMessage
from logi.models import Logi

logger = logging.getLogger(__name__)


def my_job():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    emailmessages = EmailMessage.objects.filter(status__in=[EmailMessage.STARTED, EmailMessage.CREATED])
    for email_message in emailmessages:
        # Если достигли end_date, завершить рассылку
        if email_message.end_date and current_datetime >= email_message.end_date:
            email_message.status = EmailMessage.COMPLETED
            email_message.save()
            continue  # Пропустить отправку, если end_date достигнут
        if email_message.next_send_time and current_datetime >= email_message.next_send_time:
            email_message.status = EmailMessage.STARTED
            clients = email_message.clients.all()
            try:
                server_response = send_mail(
                    subject=email_message.message.subject,
                    message=email_message.message.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in clients],
                    fail_silently=False,
                )
                Logi.objects.create(status=Logi.SUCCESS,
                                    server_response=server_response,
                                    email_message=email_message, )
            except smtplib.SMTPException as e:
                Logi.objects.create(status=Logi.FAIL,
                                    server_response=str(e),
                                    email_message=email_message, )
            if email_message.periodicity == EmailMessage.DAILY:
                email_message.next_send_time += timedelta(days=1)
            elif email_message.periodicity == EmailMessage.WEEKLY:
                email_message.next_send_time += timedelta(weeks=1)
            elif email_message.periodicity == EmailMessage.MONTHLY:
                email_message.next_send_time += timedelta(days=30)

            email_message.save()


def start_scheduler():
    scheduler = BlockingScheduler()

    # Проверка, добавлена ли задача уже
    if not scheduler.get_jobs():
        scheduler.add_job(my_job, 'interval', seconds=30)

    if not scheduler.running:
        scheduler.start()


class Command(BaseCommand):
    help = "Запускает APScheduler для отправки рассылок"

    def handle(self, *args, **options):
        logger.info("Starting scheduler...")
        start_scheduler()
        logger.info("Scheduler started. Press Ctrl+C to exit.")
        try:
            while True:
                pass
        except (KeyboardInterrupt, SystemExit):
            logger.info("Scheduler stopped.")
