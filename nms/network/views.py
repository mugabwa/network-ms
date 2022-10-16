from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from nms.network.models import Bandwidth
from nms.network.serializer import BandwidthSerializer

class BandwidthViewset(viewsets.ModelViewSet):
    serializer_class = BandwidthSerializer
    queryset = Bandwidth.objects.all()

    @action(methods=['get'], detail=True)
    def terminate(self, request, pk):
        """Terminate Connection"""
        instance = self.get_object()
        instance.terminated = True
        instance.setValid()
        instance.termination_date = timezone.now()
        instance.save()
        return Response(data='Connection terminated')
        
    @action(methods=['get'], detail=True)
    def unterminate(self, request, pk):
        """Terminate Connection"""
        instance = self.get_object()
        if instance.valid or not instance.terminated:
            return Response(data='Connection is not terminated')
        instance.terminated = False
        instance.setValid()
        instance.untermination_date = timezone.now()
        instance.save()
        return Response(data='Connection restored')