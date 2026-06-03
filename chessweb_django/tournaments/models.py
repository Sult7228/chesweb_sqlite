from django.db import models
from django.contrib.auth.models import User


class Tournament(models.Model):
    FORMAT_CHOICES = [
        ('swiss', 'Swiss'),
        ('round_robin', 'Round Robin'),
    ]

    name = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_tournaments')
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default='swiss')
    start_date = models.DateTimeField()
    participants = models.ManyToManyField(User, related_name='tournaments', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name