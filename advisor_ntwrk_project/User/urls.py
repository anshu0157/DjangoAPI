from django.urls import path,include
from . import views
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.UserRegister.as_view(),name="Register"),
    path('login/', views.UserLogin.as_view(),name="Login"),
    path('<int:uid>/advisor', views.UserAdvisor.as_view(),name="Advisor"),
    path('<int:uid>/advisor/<int:Aid>', views.UserAdvisor.as_view(),name="Advisor"),
    path('<int:uid>/advisor/booking/', views.BookedCalls.as_view(),name="Advisor"),
]