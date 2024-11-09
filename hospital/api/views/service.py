from rest_framework import viewsets, mixins
from ..models import Service
from ..serializers import (
    ServiceListSerializer,
    ServiceRetrieveSerializer,
    ServiceCreateSerializer,
    ServiceUpdateSerializer,
)

class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        if self.action == 'create':
            return ServiceCreateSerializer
        if self.action == 'update':
            return ServiceUpdateSerializer

    def get_queryset(self):
        return Service.objects.all()
