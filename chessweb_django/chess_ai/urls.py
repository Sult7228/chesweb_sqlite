from django.urls import path
from .views import chess_board, chess_local

urlpatterns = [
    path('', chess_board, name='chess_board'),
    path('local/', chess_local, name='chess_local'),
]