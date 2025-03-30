from django.contrib.auth import authenticate, logout
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def validate(self, data):
        if len(data["password"]) <= 4:
            raise serializers.ValidationError(
                "Password is too weak. It should be more than 4 characters."
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)

        return {"refresh": str(refresh), "access": str(refresh.access_token)}

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return serializers.ValidationError(
                "Both username and password are required."
            )
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        return {
            "username": user.username,
            "tokens": self.get_tokens(user),
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]

        return attrs
