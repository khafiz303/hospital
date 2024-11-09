from rest_framework import generics
from rest_framework import viewsets, mixins , filters
from django_filters.rest_framework import  DjangoFilterBackend

from ..filters import PatientFilterSet
from ..mixin import HospitalGenericViewSet
from ..models import Patient
from ..serializers import (
    PatientListSerializer,
    PatientRetrieveSerializer,
    PatientUpdateSerializer,
    PatientCreateSerializer
)


class PatientView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    filter_backends =[DjangoFilterBackend , filters.SearchFilter ]
    filterset_fields =['gender']
    filter_class = PatientFilterSet
    search_fields = ['first_name']

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve' , 'create' , 'update' , 'destroy'):
            self.action_permissions = ['patient.сan_view',]
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'retrieve':
            return PatientRetrieveSerializer
        if self.action == 'create':
            return PatientCreateSerializer
        if self.action == 'update':
            return PatientUpdateSerializer


    def get_queryset(self):
        return Patient.objects.all()

