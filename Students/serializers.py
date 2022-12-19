from dataclasses import fields
from pyexpat import model
from wsgiref import validate
from rest_framework import serializers
from Admin.models import Users
from .models import Profile
from Admin.serializers import BatchSerializers

class SignupSerializers(serializers.ModelSerializer):
    
    class Meta:
        model= Users
        fields= '__all__'

  
    def create(self,validated_data):

        adv = Users.objects.create_user(
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                email = validated_data['email'],
                domain_name = validated_data['domain_name'],
                password = validated_data['password'],
                phone = None,
                img = None,
                DOB = None,
               
            )
        # adv.set_password(validated_data['password'])
        adv.save()
        
        return adv

class SignUpBatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['batch']


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        depth = 1