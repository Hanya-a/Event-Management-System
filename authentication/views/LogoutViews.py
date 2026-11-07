from ..serializers.logout_serializer import LogoutSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class LogoutViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "Successfully logged out."},
            status=status.HTTP_200_OK
        )