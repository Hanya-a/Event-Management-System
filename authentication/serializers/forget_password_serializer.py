from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def validate(self, data):
        try:
            user= User.objects.get(email=data["email"])
        except Exception as e:
            raise serializers.ValidationError(str(e))

        data["user"] = user
        data["token"] = default_token_generator.make_token(user)
        return data
    def save(self):
        user=self.validated_data["user"]
        token=self.validated_data["token"]
        send_mail(
            subject="Password Reset",
            message = f"Your password reset token is: {token}",
            from_email=None,
            recipient_list=[user.email],
        )

