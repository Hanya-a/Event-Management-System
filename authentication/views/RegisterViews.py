from django.db.migrations import serializer
from rest_framework import viewsets,status
from ..serializers.register_serializer import RegisterSerializer
from rest_framework.response import Response

class RegisterView(viewsets.ViewSet):

    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "User registered successfully."},
            status=status.HTTP_201_CREATED
        )