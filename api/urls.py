from django.urls import path, include
from rest_framework import routers
from .views import TeamViewset, TaskViewset, LoginView, RegisterView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = routers.DefaultRouter()
router.register(r'teams', TeamViewset, basename='teams')
router.register(r'tasks', TaskViewset, basename='tasks') 

urlpatterns = [

    # For browsable API
    path('', include('rest_framework.urls')), 

    # OpenAPI schema endpoint
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc UI
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='api-login'),
    path('register/', RegisterView.as_view(), name='api-register'),
]