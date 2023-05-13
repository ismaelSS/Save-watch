from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.core import validators


class UserSerializer(serializers.ModelSerializer):
    password_validators = [
        validators.MinLengthValidator(
            8, message="The password must be at least 8 characters long."
        ),
        validators.RegexValidator(
            r"[A-Z]",
            message="The password should contain at least one uppercase character.",
        ),
        validators.RegexValidator(
            r"[a-z]", message="The password must contain at least one lowercase letter."
        ),
        validators.RegexValidator(
            r"[0-9]", message="The password must contain at least one number."
        ),
        validators.RegexValidator(
            r'[!@#$%^&*()_+=\[\]{};:\'",.<>/?\\|~-]',
            message="The password must contain at least one special character.",
        ),
    ]

    password = serializers.CharField(write_only=True, validators=password_validators)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "username",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()