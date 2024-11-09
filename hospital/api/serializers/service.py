from rest_framework import serializers
from ..models import Service

class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['description', 'cost']
