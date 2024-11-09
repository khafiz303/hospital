from rest_framework import serializers
from .models import Doctor, Service, Visit


# class DoctorListSerializer(serializers.Serializer):
#     full_name = serializers.CharField()
#     contact_info = serializers.CharField()


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields  = '__all__'

class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Doctor
        fields = '__all__'

class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization' , 'contact_info']

class PatientListSerializer(serializers.Serializer):
    full_name =serializers.CharField()
    date_of_birth = serializers.DateField()
    gender  = serializers.CharField()
    id = serializers.IntegerField()





class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class  ServiceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields  = '__all__'

class  ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Service
        fields = '__all__'

class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['description' , 'cost']



class VisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

#
class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'





