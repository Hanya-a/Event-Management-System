from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if user is None:
            raise serializers.ValidationError("Invalid username or password.")

        else:
            data['user'] = user
            return data