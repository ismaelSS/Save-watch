from rest_framework import serializers
from .models import List
from users.serializers import UserSerializer
from seasons.serializers import SeasonSerializer


class ListSerializer(serializers.ModelSerializer):
    creator = UserSerializer(required=False)
    users = UserSerializer(required=False)
    watch = SeasonSerializer(required=False)
    
    class Meta:
        model = List
        fields = [
            "id",
            "name",
            "creator"
            "users"
            "watchs"
        ]