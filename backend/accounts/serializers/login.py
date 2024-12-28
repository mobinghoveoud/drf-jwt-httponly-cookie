from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = PasswordField()
