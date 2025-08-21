from rest_framework import serializers
from .models import User,Document
from django.contrib.auth.hashers import make_password

class UserSerialzer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
    class Meta:
        model = User
        fields = '__all__'
        
class DocSeializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'