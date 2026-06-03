from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('finished', 'Finished'),
        ('draw', 'Draw'),
    ]

    white_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='white_games')
    black_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='black_games')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    pgn = models.TextField(blank=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_games')
    time_control = models.CharField(max_length=20, default='10+0')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.white_player} vs {self.black_player} — {self.status}'


class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='moves')
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    move_number = models.IntegerField()
    notation = models.CharField(max_length=10)
    fen_after = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['move_number']

    def __str__(self):
        return f'Move {self.move_number}: {self.notation}'