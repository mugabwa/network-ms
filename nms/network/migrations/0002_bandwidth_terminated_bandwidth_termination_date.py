# Generated by Django 4.1.1 on 2022-10-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandwidth',
            name='terminated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bandwidth',
            name='termination_date',
            field=models.DateTimeField(null=True),
        ),
    ]