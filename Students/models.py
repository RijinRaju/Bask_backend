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
