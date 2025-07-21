from django.shortcuts import render
from rest_framework import viewsets, exceptions
from .models import Team, Task
from .serializers import TeamSerializer, TaskSerializer


# Create your views here.
class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def partial_update(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed('PATCH')

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def partial_update(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed('PATCH')