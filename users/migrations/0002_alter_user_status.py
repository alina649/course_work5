# Generated by Django 4.2.5 on 2023-09-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('active', 'активен'), ('blocked', 'заблокирован')], default='active', max_length=15, verbose_name='статус пользователя'),
        ),
    ]
