# Generated by Django 4.1.1 on 2022-10-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_bandwidth_terminated_bandwidth_termination_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandwidth',
            name='untermination_date',
            field=models.DateTimeField(null=True),
        ),
    ]