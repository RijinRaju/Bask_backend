from dataclasses import field, fields
from pyexpat import model
from .models import Domain,Batch, Task, Users
from rest_framework import serializers

class DomainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields='__all__'


class BatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
        


class BatchSerializersRead(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
        read_only_fields=['batch_advisor']
        depth = 1

class AdvisorsSerializers(serializers.ModelSerializer):

    class Meta:
        model= Users
        fields = '__all__'
    
    def create(self,validated_data):
        adv = Users.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            phone  = validated_data['phone'],
            img = validated_data['img'],
            DOB = validated_data['DOB'],
            password = validated_data['password']
        )
        adv.save()
        
        return adv


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        depth = 1