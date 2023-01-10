# chat/routing.py
from django.urls import re_path,path

from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<int:room_name>/<int:sender>/<int:enduser>/", consumers.ChatConsumer.as_asgi()),
    path('ws/notifications/',consumers.NotificationConsumer.as_asgi()),
]
