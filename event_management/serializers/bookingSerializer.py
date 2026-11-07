from rest_framework import serializers
from ..models.bookingModel import Booking

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model= Booking
        fields = '__all__'

    def validate(self, data):
        attendee = data['attendee']
        event = data['event']

        if attendee.balance < event.price:
            raise serializers.ValidationError(
                "Insufficient balance to book this event."
            )
        if event.booking_set.count() >= event.capacity:
            raise serializers.ValidationError(
                "This event is full."
            )
        if Booking.objects.filter(attendee=attendee, event=event).exists():
            raise serializers.ValidationError(
                "This attendee has already booked this event."
            )
        return data
