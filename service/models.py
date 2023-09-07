from django.db import models

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

    FREQUENCY_CHOICE = (
        ('daily', 'ежедневно'),
        ('weekly', "еженедельно"),
        ('monthly', "ежемесячно")
    )

    STATUS_CHOICE = (
        ('completed', "завершено"),
        ('created', "создано"),
        ('commenced', "запущено")
    )

    client = models.ManyToManyField(Client, verbose_name='Клиенты', blank=False)
    message = models.ForeignKey(Message, verbose_name='Письма', on_delete=models.CASCADE, blank=False,
                                limit_choices_to={'is_active': True})
    mailing_time = models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки')
    frequency = models.CharField(choices=FREQUENCY_CHOICE, default='daily', max_length=10, verbose_name='Периодичность рассылки')
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default='created', verbose_name='Статус рассылки')

    def __str__(self):
        return f"Рассылка #{self.pk} время рассылки"

    class Meta:
        verbose_name_plural = "Рассылки"


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
    status = models.CharField(choices=STATUS_CHOICE, max_length=20, verbose_name='Статус попытки рассылки')
    response = models.CharField(verbose_name='Ответ почтового сервера')

    def __str__(self):
        return f"Лог рассылки # {self.timestamp} - {self.status}"

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"
