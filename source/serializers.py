
from rest_framework import serializers
from .models import Source

class SourceSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
