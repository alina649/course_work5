# Generated by Django 4.2.4 on 2023-08-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_mailinglogs_options_mailinglogs_mailing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglogs',
            name='response',
            field=models.CharField(verbose_name='Ответ почтового сервера'),
        ),
    ]