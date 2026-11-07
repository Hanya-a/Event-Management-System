from rest_framework.routers import DefaultRouter

from .views.attendeeView import AttendeeViewSet
from .views.bookingView import BookingViewSet
from .views.eventView import EventViewSet

router = DefaultRouter()

router.register('attendees', AttendeeViewSet, basename='attendee')
router.register('bookings', BookingViewSet, basename='booking')
router.register('events', EventViewSet, basename='event')

urlpatterns = router.urls