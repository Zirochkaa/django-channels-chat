from django.contrib import admin

from .models import Message, Room


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('get_room', 'user', 'content', 'date_added',)

    @admin.display(description='Room')
    def get_room(self, obj):
        return obj.room.name

    def get_queryset(self, request):
        return Message.objects.select_related('user', 'room')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
