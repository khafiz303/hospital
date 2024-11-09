from rest_framework import serializers
from ..models import Visit, Schedule
from rest_framework.exceptions import ValidationError


class VisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit  # Changed model to Visit
        fields = '__all__'





class VisitCreateSerializer(serializers.ModelSerializer):
    def validate_schedule(self, value):
        visit_count = value.visit.count()  # Подразумевается, что у Schedule есть обратная связь с Visit

        if visit_count >= 3:
            raise ValidationError('Максимальное количество визитов для данного расписания достигнуто.')
        return value


    class Meta:
        model = Visit
        fields = ['patient', 'schedule', 'service' , 'visit_date_time']

class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit  # Changed model to Visit
        fields = '__all__'




class VisitRatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value =0 , max_value = 10)
    def validate_rating(self, value):
        if self.instanse.rating_set:
            raise ValidationError('вы уже ставили рейтнинг')

    class Meta:
        model = Visit
        fields = ['rating']
