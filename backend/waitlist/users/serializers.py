from rest_framework import serializers
from .models import User


class SuscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['suscriber_id', 'email', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
