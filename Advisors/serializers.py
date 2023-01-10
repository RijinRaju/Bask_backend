from Students.models import Messages 
from rest_framework import serializers
from Admin.models import Allocate, Manifest



class ManifestUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manifest
        fields = '__all__'


class ManifestViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manifest
        fields = '__all__'
        depth = 1
        

class ChatListSerializers(serializers.ModelSerializer):
    class Meta:
        model= Allocate
        fields = "__all__"
        depth = 1

class RecordChatSerializers(serializers.ModelSerializer):
    class Meta:
        model= Messages
        fields = "__all__"
        depth = 1
        