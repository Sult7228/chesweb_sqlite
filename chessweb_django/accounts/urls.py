from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterAPIView, ProfileDetailView, MyProfileView, register_page
from .views import RegisterAPIView, ProfileDetailView, MyProfileView, register_page, logout_view
from .views import RegisterAPIView, ProfileDetailView, MyProfileView, register_page, logout_view, login_page

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('profile/<int:pk>/', ProfileDetailView.as_view()),
    path('profile/me/', MyProfileView.as_view()),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_view, name='logout'),
]