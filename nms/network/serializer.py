from rest_framework import serializers

from nms.network.models import Bandwidth

class BandwidthSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ['client','package','start_date','valid']
        fields = '__all__'
        model = Bandwidth

    def create(self, validated_data):
        bandwidth = Bandwidth.objects.create(**validated_data)
        return bandwidth