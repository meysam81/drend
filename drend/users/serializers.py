from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'email': {'required': True},
        }
