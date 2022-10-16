from rest_framework import viewsets

from nms.payment.models import Invoices
from nms.payment.serializer import InvoicesSerializer

class InvoicesViewset(viewsets.ModelViewSet):
    serializer_class = InvoicesSerializer
    queryset = Invoices.objects.all()
