from rest_framework import serializers
from .models import Team, Task


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