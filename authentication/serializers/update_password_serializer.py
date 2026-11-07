from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator



class UpdatePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True)
    user_id = serializers.IntegerField()
    token = serializers.CharField()

    def validate(self,data):
        self.user = User.objects.get(id=data["user_id"])
        if not default_token_generator.check_token(self.user, data["token"]):
            raise serializers.ValidationError("Invalid or expired reset token.")
        return data

    def update(self,user,validated_Data):
        self.user.set_password(validated_Data["new_password"])
        self.user.save()
        return user
