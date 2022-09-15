from nms.client.models import Clients
import pytest

@pytest.mark.django_db
def test_clients_model():
    Clients.objects.create(
        first_name = 'Amos',
        last_name = 'Masibo',
        location = 'Githurai 44',
        contacts = '0712345678',
    )
    clients = Clients.objects.get(
        first_name = 'Amos', last_name = 'Masibo', location = 'Githurai 44')
    assert clients.custom_unique_feild == 'amos/masibo/githurai_44'
    # assert Clients.objects.filter(
    #     custom_unique_feild = 'amos/masibo/githurai_44').exists()