from rest_framework import serializers
from django.conf import settings
from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'content']
    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value