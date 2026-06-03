from rest_framework import serializers
from .models import Game, Move


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'
        read_only_fields = ('player', 'move_number', 'fen_after', 'timestamp')


class GameSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('status', 'winner', 'pgn', 'created_at')