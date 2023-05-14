from rest_framework import serializers
from .models import Season
from watch.serializers import WatchSerializer


class SeasonSerializer(serializers.ModelSerializer):
    watch = WatchSerializer(required=False)
    class Meta:
        model = Season
        fields = [
            "id",
            "image",
            "is_dubbed"
            "watch"
        ]