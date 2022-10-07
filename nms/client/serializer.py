from rest_framework import serializers
from nms.client.models import Clients

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = ['first_name', 'last_name','location','contacts','status','date_joined']

    def create(self, validated_data):
        client = Clients.objects.create(**validated_data)
        return client
