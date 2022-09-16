import pytest
from model_bakery import baker
from datetime import timedelta

from django.utils import timezone

from nms.client.models import Clients
from nms.network.models import Bandwidth

@pytest.mark.django_db
def test_payment_model():
    client = baker.make(
        Clients, first_name = 'Amos', last_name = 'Masibo',
        location = 'Githurai 44')
    current_start_date = timezone.now()-timedelta(days=5)

    baker.make(
        Bandwidth, client=client, package=20,
        start_date=current_start_date)

    clients = Clients.objects.filter(
        custom_unique_feild = 'amos/masibo/githurai_44')
    bandwidth = Bandwidth.objects.filter(
        client = clients[0]
    )

    assert clients.exists() == True
    assert bandwidth.exists() == True
    assert bandwidth[0].start_date == current_start_date
    assert bandwidth[0].end_date == current_start_date+timedelta(days=30)
    assert bandwidth[0].valid == True

@pytest.mark.django_db
def test_payment_model_invalid():
    client = baker.make(
        Clients, first_name = 'Amos', last_name = 'Masibo',
        location = 'Githurai 44')
    current_start_date = timezone.now()-timedelta(days=50)

    baker.make(
        Bandwidth, client=client, package=20,
        start_date=current_start_date)

    clients = Clients.objects.filter(
        custom_unique_feild = 'amos/masibo/githurai_44')
    bandwidth = Bandwidth.objects.filter(
        client = clients[0]
    )

    assert clients.exists() == True
    assert bandwidth.exists() == True
    assert bandwidth[0].start_date == current_start_date
    assert bandwidth[0].end_date == current_start_date+timedelta(days=30)
    assert bandwidth[0].valid == False