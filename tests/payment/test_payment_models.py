from nms.client.models import Clients
from nms.payment.models import Invoices

from model_bakery import baker
import pytest

@pytest.mark.django_db
def test_payment_model():
    client = baker.make(
        Clients, first_name = 'Amos', last_name = 'Masibo',
        location = 'Githurai 44')
    baker.make(
        Invoices, client=client, amount=2000,
        reference_number='X12345Y' 
    )

    clients = Clients.objects.filter(
        custom_unique_feild = 'amos/masibo/githurai_44')
    invoices = Invoices.objects.filter(
        client = clients[0]
    )

    assert clients.exists() == True
    assert invoices.exists() == True
    assert invoices[0].amount == 2000.00
    assert invoices[0].reference_number == 'X12345Y'