from rest_framework import viewsets,status
from ..serializers.update_password_serializer import UpdatePasswordSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

class UpdatePasswordView(viewsets.ViewSet):

    def partial_update(self,request,pk):
        user = User.objects.get(id=pk)
        serializer = UpdatePasswordSerializer(
            user,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password reset successfully."},
        status=status.HTTP_200_OK
        )