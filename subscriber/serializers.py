
from rest_framework import serializers
from .models import Subscriber

class SubscriberSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'
        depth = 2


