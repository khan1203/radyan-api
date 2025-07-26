from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Task

import pprint


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    confirm = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
    
    def validate(self, data):
        # pprint.pprint(data)
        if(data['password']!=data['confirm_password']):
            raise serializers.ValidationError({'confirm_password' : 'Password do not match.'})
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username = validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user