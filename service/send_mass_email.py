import os
import django
import datetime
from service.models import Mailing, MailingLogs
import pytz
from django.core.mail import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def send_mails():
    now = datetime.datetime.now()
    for mailing in Mailing.objects.filter(mailing_status=Mailing.STATUS_STARTED):
        for client in mailing.clients.all():
            mailing_log = MailingLogs.objects.filter(log_client=client, log_mailing=mailing)
            if mailing_log.exists():
                last_try = mailing_log.order_by('-created_time').first()
                desired_timezone = pytz.timezone('Europe/Moscow')
                last_try_date = last_try.created_time.astimezone(desired_timezone)
                if mailing.PERIOD_DAILY:
                    if (now.date() - last_try_date.date()).days >= 1:
                        send_mail(mailing, client)
                elif mailing.PERIOD_WEEKLY:
                    if (now.date() - last_try_date.date()).days >= 7:
                        send_mail(mailing, client)
                elif mailing.PERIOD_MONTHLY:
                    if (now.date() - last_try_date.date()).days >= 30:
                        send_mail(mailing, client)
            else:
                send_mail(mailing, client)