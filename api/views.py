from django.shortcuts import render
from rest_framework import viewsets, exceptions
from .models import Team, Task
from .serializers import TeamSerializer, TaskSerializer


# Create your views here.
class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete']