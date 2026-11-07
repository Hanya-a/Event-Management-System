from rest_framework import viewsets,status
from ..serializers.forget_password_serializer import ForgetPasswordSerializer
from rest_framework.response import Response

class ForgetPasswordView(viewsets.ViewSet):

    def create(self, request):
        serializer =  ForgetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "detail": "If an account exists for this email, a password reset email has been sent."
            }
        )