from django.urls import path
from .views import GameListCreateView, GameDetailView, make_move, resign

urlpatterns = [
    path('games/', GameListCreateView.as_view()),
    path('games/<int:pk>/', GameDetailView.as_view()),
    path('games/<int:pk>/move/', make_move),
    path('games/<int:pk>/resign/', resign),
]