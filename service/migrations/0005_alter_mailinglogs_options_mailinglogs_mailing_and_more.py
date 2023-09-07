# Generated by Django 4.2.4 on 2023-08-20 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_mailing_client_mailing_message_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailinglogs',
            options={'verbose_name': 'Лог', 'verbose_name_plural': 'Логи'},
        ),
        migrations.AddField(
            model_name='mailinglogs',
            name='mailing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.mailing', verbose_name='Рассылка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mailinglogs',
            name='response',
            field=models.TextField(default=1, verbose_name='Ответ почтового сервера'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mailinglogs',
            name='status',
            field=models.CharField(choices=[('success', 'успешно'), ('mistake', 'ошибка')], max_length=20, verbose_name='Статус попытки рассылки'),
        ),
    ]
