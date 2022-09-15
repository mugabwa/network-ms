# Generated by Django 4.1.1 on 2022-09-14 17:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_alter_clients_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('payment_contacts', models.CharField(max_length=20)),
                ('amount', models.DecimalField(
                    decimal_places=2, max_digits=10)),
                ('is_cash', models.BooleanField(default=False)),
                ('date_payed', models.DateTimeField(
                    verbose_name=django.utils.timezone.now)),
                ('reference_number', models.CharField(
                    max_length=20, null=True)),
                ('client', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='client.clients')),
            ],
        ),
    ]
