from django.urls import path, include
from rest_framework import routers
from .views import TeamViewset, TaskViewset
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('', include('rest_framework.urls')),  # For browsable API

    # OpenAPI schema endpoint
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc UI
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

routers = routers.DefaultRouter()
routers.register(r'teams', TeamViewset, basename='teams')
routers.register(r'tasks', TaskViewset, basename='tasks') 
urlpatterns += routers.urls