from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Tournament
from .serializers import TournamentSerializer


class TournamentListCreateView(generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def join_tournament(request, pk):
    try:
        tournament = Tournament.objects.get(pk=pk)
    except Tournament.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    tournament.participants.add(request.user)
    return Response({'status': 'joined'})