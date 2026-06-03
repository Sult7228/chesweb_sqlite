from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Game, Move
from .serializers import GameSerializer, MoveSerializer
from .services import validate_and_apply_move


class GameListCreateView(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(
            white_player=self.request.user
        ) | Game.objects.filter(
            black_player=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(white_player=self.request.user)


class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def make_move(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response({'error': 'Game not found'}, status=404)

    if game.status != 'ongoing':
        return Response({'error': 'Game is already finished'}, status=400)

    notation = request.data.get('notation')
    valid, fen = validate_and_apply_move(game, notation)

    if not valid:
        return Response({'error': 'Invalid move'}, status=400)

    move_number = game.moves.count() + 1
    Move.objects.create(
        game=game,
        player=request.user,
        move_number=move_number,
        notation=notation,
        fen_after=fen
    )
    return Response({'status': 'ok', 'fen': fen})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def resign(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response({'error': 'Game not found'}, status=404)

    if request.user == game.white_player:
        game.winner = game.black_player
    else:
        game.winner = game.white_player

    game.status = 'finished'
    game.save()
    return Response({'status': 'resigned'})