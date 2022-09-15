from django.db import models
from django.utils import timezone

from nms.client.models import Clients


class Invoices(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    payment_contacts = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_cash = models.BooleanField(default=False)
    date_payed = models.DateTimeField(timezone.now)
    reference_number = models.CharField(max_length=20, null=True)
