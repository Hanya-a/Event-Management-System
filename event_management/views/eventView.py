from ..models.eventModel import Event
from ..serializers.eventSerializer import EventSerializer
from rest_framework import viewsets
from  rest_framework.permissions import IsAuthenticated
from authentication.custom_permissions.IsAdminOrReadOnly import IsAdminOrReadOnly

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadOnly]

    filterset_fields = ['location', 'capacity', 'price']
    search_fields = ['name', 'description', 'location']
    ordering_fields = ['name', 'date', 'price', 'capacity']
