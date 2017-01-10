from django.contrib import admin
from.models import Robot


@admin.register(Robot)
class AdminRobot(admin.ModelAdmin):
    list_display = ["name", "price"]
