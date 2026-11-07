from django.db import models
from .attendeeModel import Attendee
from .eventModel import Event

class Booking(models.Model):

    PAYMENT_METHODS = [
        ('visa', 'Visa'),
        ('instapay', 'InstaPay'),
        ('apple_pay', 'Apple Pay'),
    ]

    attendee = models.ForeignKey(Attendee,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20,choices=PAYMENT_METHODS)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['attendee', 'event'],
                name='no_duplicate_bookings'
            )
        ]