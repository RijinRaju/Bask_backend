from operator import mod
from django.db import models
from Admin.models import Batch,Users
from Admin.serializers import AdvisorsSerializers
from Admin.models import MyAccountManager
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    profile_img = models.FileField(upload_to='Frontend/src/Assests/Profiles',verbose_name='profile',null=True)
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)


class Notifications(models.Model):
    user_sender = models.ForeignKey(Users,null=True,blank=True,related_name='user_sender', on_delete=models.CASCADE)
    user_revoker = models.ForeignKey(Users,null=True,blank=True,related_name='user_revoker', on_delete=models.CASCADE)
    status = models.CharField(max_length=264,null=True,blank=True,default='unread')
    type_of_notification = models.CharField(max_length=264,null=True,blank=True)



class Room(models.Model):
    room_name =  models.CharField(max_length=150,null=True)
    sender = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True, related_name="sender")
    receiver = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True, related_name="receiver")


class Messages(models.Model):
    room_name = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    sender = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    message = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add = True) 


class PersonalDetails(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    dob = models.CharField(max_length=150,null=True)
    age = models.IntegerField(default=0,null=True)
    gender = models.CharField(max_length=150,null=True)
    father_name = models.CharField(max_length=200,null=True)
    father_contact = models.CharField(max_length=200,null=True)
    mother_name = models.CharField(max_length=200,null=True)
    mother_contact = models.CharField(max_length=200,null=True)
    address = models.TextField(null=True)
    village = models.CharField(max_length=200,null=True)
    taluk = models.CharField(max_length=200,null=True)
    education_qualification = models.CharField(max_length=200,null=True)
    collage_or_school = models.CharField(max_length=200,null=True)