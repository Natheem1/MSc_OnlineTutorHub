from django.contrib import admin
from .models import Topic, Room, ChatMessage

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(ChatMessage)