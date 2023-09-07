# Generated by Django 4.2.4 on 2023-08-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('full_name', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_time', models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки')),
                ('frequency', models.CharField(max_length=10, verbose_name='Периодичность рассылки')),
                ('status', models.CharField(default='created', max_length=10, verbose_name='Статус рассылки')),
            ],
            options={
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('status', models.CharField(max_length=20, verbose_name='Статус попытки рассылки')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера')),
            ],
            options={
                'verbose_name_plural': 'Логи рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='Тема письма')),
                ('body', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name_plural': 'Сообщение для рассылки',
            },
        ),
    ]
