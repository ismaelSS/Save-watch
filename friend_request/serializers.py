from rest_framework import serializers
from .models import FriendRequest
from users.serializers import UserSerializer


class FriendRequestSerializer(serializers.ModelSerializer):
    senders = UserSerializer(required=False)
    receivers = UserSerializer(required=False)
    
    class Meta:
        model = FriendRequest
        fields = [
            "id",
            "senders",
            "receivers"
        ]