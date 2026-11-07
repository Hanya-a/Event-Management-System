from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = RefreshToken(data['refresh'])
        return data

    def save(self):
        self.token.blacklist()