from functools import partial
from logging import raiseExceptions
from rest_framework.response import Response

from rest_framework import viewsets, mixins, status
from ..models import Visit
from ..serializers import (
    VisitListSerializer,
    VisitRetrieveSerializer,
    VisitCreateSerializer,
    VisitUpdateSerializer,
    VisitRatingSerializer
)



class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_visit',]
        elif self.action == 'create':
            self.action_permissions = ['add-visit',]
        # elif self.action == 'update':
        #     self.action_permissions = ['change-visit', ]
        # elif self.action == 'destroy':
        #     self.action_permissions = ['delete-visit', ]
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'update':
            return VisitUpdateSerializer
        if self.action == 'set_rating':
            return VisitRatingSerializer

    def get_queryset(self):
        return Visit.objects.all()

    def set_rating(self, request, id=None):
        instance = self.get_object()  # По умолчанию DRF использует `pk` для поиска объекта
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)



