# chat/consumers.py
import json
from django.dispatch import receiver
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Messages
from Admin.models import Users
from .models import Room
from django.core import serializers

class ChatConsumer(AsyncWebsocketConsumer):




    @database_sync_to_async
    def save_room(self,room_name,sender,enduser):
        sender_instance = Users.objects.get(id=sender)
        receiver_instance = Users.objects.get(id=enduser)
        if Room.objects.filter(room_name=room_name).exists():
            try:
                self.room_id = Room.objects.get(
                    sender=sender_instance, receiver=receiver_instance)
            except:
               self.room_id = Room.objects.get(sender=receiver_instance, receiver=sender_instance)
            #   Room.objects.get(room_name=room_name, sender=sender_instance)
            return self.room_id
        self.room_id  = Room.objects.create(room_name=room_name,sender=sender_instance,receiver=receiver_instance) 
        return self.room_id

    @database_sync_to_async
    def save_chat(self,msg,sender):
        sender_instance = Users.objects.get(id=sender)
        self.chat = Messages.objects.create(room_name=self.room_id,message=msg,sender=sender_instance)
        return self.chat


    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]  #room name is the receiver
        self.sender = self.scope["url_route"]["kwargs"]["sender"]
        self.enduser = self.scope["url_route"]["kwargs"]["enduser"]
        self.room_group_name = "notification_%s" % self.room_name
        # Join room group
        await self.channel_layer.group_add(
             self.room_group_name,
             self.channel_name,
             )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
            )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(self.enduser)
        create_room  = await self.save_room(self.room_name,self.sender,self.enduser)
        new_messages = await self.save_chat(message,self.sender)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "send_message",
             "message": message,
             }
        )
        print(message)


    async def send_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message":message,
            "receiver":self.enduser,
            }))


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        pass

    
    async def receive(self,text_data):
        self.send(text_data = "you said"+ text_data)

    
    async def send_notification(self, event):
        await self.send(text_data = event['new task added'])
