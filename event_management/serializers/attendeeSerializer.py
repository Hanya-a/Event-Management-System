from rest_framework import serializers
from ..models.attendeeModel import Attendee

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Attendee
        fields = '__all__'
