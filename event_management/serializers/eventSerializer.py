from ..models.eventModel import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):

    def validate_capacity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Capacity must be greater than 0."
            )
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )
        return value

    class Meta:
        model = Event
        fields = '__all__'

