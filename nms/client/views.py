from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from nms.client.models import Clients
from nms.client.serializer import ClientSerializer
from nms.common.configurations.paginator import CustomPagination

class ClientViewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Clients.objects.all()
    pagination_class = CustomPagination

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        return Response(data='Client deleted successfully')