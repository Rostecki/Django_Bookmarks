from django.contrib import admin
from django.db.models.deletion import PROTECT
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'data_urodzenia', 'zdjęcie']