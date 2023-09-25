from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from service.models import Mailing, MailingLogs, Client
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def get_next_date(repeat, old_date):
    # print(repeat)
    # print(old_date)
    next_date = None
    if repeat == 'daily':
        next_date = old_date + timedelta(days=1)
    elif repeat == 'weekly':
        next_date = old_date + timedelta(weeks=1)
    elif repeat == 'monthly':
        next_date = old_date + relativedelta(months=1)
    # print(next_date)
    return next_date


def send_mailing():
    now = timezone.now()

    mailing_to_send = Mailing.objects.all()
    print(mailing_to_send)
    for mailing in mailing_to_send:
        if mailing.get_status() == 'running':
            print(mailing.frequency)
            clients = [client.email for client in Client.objects.filter(mailing=mailing.pk)]
            print(clients)
            try:
                result = send_mail(
                    subject=mailing.title,
                    message=mailing.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=clients
                )

            except:
                result = False

            if result:
                status = 'success'
            else:
                status = 'mistake'
            mailing_log = MailingLogs.objects.create(mailing=mailing)
            mailing_log.status = status
            mailing_log.last_try = now
            mailing.status = 'created'
            mailing.next_start = get_next_date(mailing.frequency, mailing.next_start)
            mailing.save()
            mailing_log.save()