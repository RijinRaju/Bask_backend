from rest_framework import serializers
from Admin.models import Allocate, Answers, Task, Users
from .models import PersonalDetails, Profile
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

class TaskViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProfileUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class BatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Allocate
        fields = '__all__'
        depth = 1

class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"

class DetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = "__all__"