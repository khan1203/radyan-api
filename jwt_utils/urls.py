from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, LoginView

urlpatterns = [

    path('api/auth/register/', RegisterView.as_view(), name='register_api'),
    path('api/auth/login/', LoginView.as_view(), name='login_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]