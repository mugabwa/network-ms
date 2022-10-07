from rest_framework import viewsets
from rest_framework.response import Response
from nms.network.models import Bandwidth
from nms.network.serializer import BandwidthSerializer

class BandwidthViewset(viewsets.ModelViewSet):
    serializer_class = BandwidthSerializer
    queryset = Bandwidth.objects.all()

    def list(self, request):
        serializer = BandwidthSerializer(self.queryset, many=True)
        return Response(serializer.data)