from ..models.attendeeModel import Attendee
from ..serializers.attendeeSerializer import AttendeeSerializer
from rest_framework import viewsets
from  rest_framework.permissions import IsAuthenticated

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [IsAuthenticated]