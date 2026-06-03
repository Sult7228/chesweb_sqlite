from django.urls import path
from .views import TournamentListCreateView, join_tournament

urlpatterns = [
    path('tournaments/', TournamentListCreateView.as_view()),
    path('tournaments/<int:pk>/join/', join_tournament),
]