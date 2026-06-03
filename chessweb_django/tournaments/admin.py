from django.contrib import admin
from .models import Tournament


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'organizer', 'format', 'start_date', 'is_active')
    list_filter = ('format', 'is_active')
    search_fields = ('name',)
    filter_horizontal = ('participants',)