from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import time, datetime

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Клиент сервиса"""

    email = models.EmailField(verbose_name='почта', unique=True)
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    """Сообщение для рассылки"""
    subject = models.CharField(max_length=200, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return f'Тема {self.subject}, текст письма {self.body}'

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = 'Письма'


class Mailing(models.Model):
    """Рассылка (настройки)"""

    FREQUENCY_CHOICES = [
        ('daily', 'ежедневно'),
        ('weekly', 'еженедельно'),
        ('monthly', 'ежемесячно'),
    ]

    STATUS_CHOICES = [
        ('created', 'создана'),
        ('running', 'запущена'),
        ('completed', 'завершена'),
    ]

    clients = models.ManyToManyField(Client, verbose_name='Клиенты', blank=False)

    start_time = models.TimeField(default=timezone.now, verbose_name='Время запуска рассылки')
    next_start = models.DateField(default=timezone.now, verbose_name='дата запуска рассылки')
    stop_time = models.TimeField(default=timezone.now, verbose_name='Время завершения рассылки')

    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='created', verbose_name='Статус рассылки')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    title = models.CharField(max_length=200, verbose_name='Название рассылки')
    body = models.TextField(verbose_name='Тело письма')
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')

    def get_status(self):
        now = datetime.now().time()
        print(self.start_time)
        print(now)
        print(self.stop_time)
        if self.start_time < now < self.stop_time:
            self.status = "running"

            self.save()
        return self.status

    def __str__(self):
        return f'{self.frequency}'

    class Meta:
        verbose_name ='Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingLogs(models.Model):
    """Логи рассылки"""

    STATUS_CHOICE = (
        ('success', 'успешно'),
        ('mistake', 'ошибка'),
    )

    RESPONSE_CHOICE = (
        ('success', 'получен'),
        ('mistake', 'не получен'),
    )

    mailing = models.ForeignKey(Mailing, verbose_name='Рассылка', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    status = models.CharField(choices=STATUS_CHOICE, default='success', max_length=20, verbose_name='Статус попытки рассылки')
    response = models.CharField(verbose_name='Ответ почтового сервера')

    def __str__(self):
        return f"Лог рассылки # {self.timestamp} - {self.status}"

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"
