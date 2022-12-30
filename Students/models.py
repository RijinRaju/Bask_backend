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


