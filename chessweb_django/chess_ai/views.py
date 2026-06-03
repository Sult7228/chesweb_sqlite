from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def chess_board(request):
    return render(request, 'chess_ai/board.html')


def chess_local(request):
    return render(request, 'chess_ai/local.html')