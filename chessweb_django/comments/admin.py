from django.contrib import admin
from .models import GameComment


@admin.register(GameComment)
class GameCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'game', 'move_number', 'created_at')
    search_fields = ('author__username',)
    list_filter = ('game',)