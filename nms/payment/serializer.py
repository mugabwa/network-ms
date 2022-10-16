from rest_framework import serializers
from nms.payment.models import Invoices

class InvoicesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Invoices

    def create(self, validated_data):
        invoices = Invoices.objects.create(**validated_data)
        invoices.reference_number = invoices.reference_number.upper()
        return invoices
