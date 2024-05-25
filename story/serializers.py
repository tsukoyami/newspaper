

from rest_framework import serializers
from .models import Story

class StorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'