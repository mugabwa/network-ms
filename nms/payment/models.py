from django.db import models
from django.utils import timezone

from nms.client.models import Clients
from nms.network.models import Bandwidth


class Invoices(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    package = models.OneToOneField(Bandwidth, on_delete=models.CASCADE, null=True)
    payment_contacts = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_cash = models.BooleanField(default=False)
    date_payed = models.DateTimeField(default=timezone.now)
    reference_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        output = (str(self.package) or str(self.client)) + ' ' + self.amount
        return output