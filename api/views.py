from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Team, Task
from .serializers import TeamSerializer, TaskSerializer, RegisterSerializer


# Create your views here.

class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if(serializer.is_valid()):
            userRetrieved = User.objects.get(username=user.data["username"])
            userRetrieved.set_password(user.data["password"])
            
            user = userRetrieved.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response (serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)