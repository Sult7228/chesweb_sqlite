from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'country')
    search_fields = ('user__username', 'country')
    list_filter = ('country',)