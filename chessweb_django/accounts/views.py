from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from .models import Profile
from .serializers import RegisterSerializer, ProfileSerializer
from django.contrib.auth import login, logout
from django.contrib.auth import login, logout, authenticate


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]


class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


def register_page(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        if not username or not password:
            error = 'Заполните все поля'
        elif User.objects.filter(username=username).exists():
            error = 'Пользователь с таким именем уже существует'
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('/')
    return render(request, 'accounts/register.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/')

def login_page(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            error = 'Неверное имя пользователя или пароль'
    return render(request, 'accounts/login.html', {'error': error}) 