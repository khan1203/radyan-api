from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from .views import TeamViewset, TaskViewset

schema_view = get_schema_view(title='radyan-api')

urlpatterns = [
    path('', include('rest_framework.urls')),  # For browsable API
    path('schema/', schema_view, name='api-schema'),
    path('docs/', include_docs_urls(title='radyan-api')),
]

routers = routers.DefaultRouter()
routers.register(r'teams', TeamViewset, basename='teams')
routers.register(r'tasks', TaskViewset, basename='tasks') 
urlpatterns += routers.urls