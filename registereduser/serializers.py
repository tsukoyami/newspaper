
from rest_framework import serializers
from .models import RegisteredUser
from company.serializers import CompanySerializer

class RegistereduserSerialiser(serializers.ModelSerializer):
    company = CompanySerializer(many=True)
    class Meta:
        model = RegisteredUser
        fields = '__all__'
        








# from rest_framework import serializers
# from .models import Company

# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = '__all__'
