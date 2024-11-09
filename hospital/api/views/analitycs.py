from ..mixin import HospitalGenericViewSet
from ..models import Patient, Doctor
from ..service import get_upcoming_visits_count
from rest_framework.response import Response
from rest_framework import status


class AnalyticsView(HospitalGenericViewSet):
    def get_action_permissions(self):
        if self.action == 'get_analytics':  # Исправлено имя действия
            self.action_permissions = []  # Убедитесь, что это нужно

    def get_analitycs(self, request):
        response = {
            'patient_count': Patient.objects.count(),  # Упрощено
            'doctor_count': Doctor.objects.count(),  # Упрощено
            'visit_count': get_upcoming_visits_count()
        }
        return Response(status=status.HTTP_200_OK, data=response)
