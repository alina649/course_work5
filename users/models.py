from django.contrib.auth.models import AbstractUser
from django.db import models

from service.models import NULLABLE


# Create your models here.

class User(AbstractUser):
    STATUS_ACTIVE = 'active'
    STATUS_BLOCKED = 'blocked'
    STATUSES = [
        (STATUS_ACTIVE, 'активен'),
        (STATUS_BLOCKED, 'заблокирован'),
    ]

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    email_confirmed = models.BooleanField(default=False, verbose_name='подтверждено')
    email_key = models.CharField(max_length=30, verbose_name='код подтверждения почты', **NULLABLE)

    status = models.CharField(max_length=15, choices=STATUSES, default=STATUS_ACTIVE,
                              verbose_name='статус пользователя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []