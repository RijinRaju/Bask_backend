from pyexpat import model
from Advisors.models import Reports
from Students.models import Messages 
from rest_framework import serializers
from Admin.models import Allocate, Manifest,Batch



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
class BatchListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"

class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = "__all__"