# Generated by Django 4.1.1 on 2022-09-14 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]