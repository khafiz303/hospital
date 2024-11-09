from django_filters import rest_framework as filters

from .models import Doctor, Patient


class DoctorFilterSet(filters.FilterSet):
    last_name = filters.CharFilter(field_name = 'last_name')

    class Meta:
        model = Doctor
        fields = {
            'last_name': ['exact' , 'icontains']
        }


# class PatientFilterSet(filters.FilterSet):
#     last_name = filters.CharFilter(field_name = 'last_name')
#
#     class Meta:
#         model = Patient
#         fields = {
#             'last_name': ['exact' , 'icontains']
#         }
class PatientFilterSet(filters.FilterSet):
    # Фильтр для фамилии, который ищет подстроку
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='icontains', label='Фамилия содержит')

    class Meta:
        model = Patient
        fields = {
            'last_name': ['icontains'],  # Ищем по подстроке
        }
