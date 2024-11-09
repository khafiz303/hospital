from rest_framework import serializers
from ..models import Doctor, Patient

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'contact_info']

# class PatientListSerializer(serializers.Serializer):
#     full_name = serializers.CharField()
#     date_of_birth = serializers.DateField()
#     gender = serializers.CharField()
#     id = serializers.IntegerField()
