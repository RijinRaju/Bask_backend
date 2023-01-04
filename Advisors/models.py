from Admin.models import Users
from django.db import models

# Create your models here.

class Week(models.Model):
    week1 = models.CharField(max_length=150,null=True)
    week2 = models.CharField(max_length=150,null=True)
    week3 = models.CharField(max_length=150,null=True)
    week4 = models.CharField(max_length=150,null=True)
    week5 = models.CharField(max_length=150,null=True)
    week6 = models.CharField(max_length=150,null=True)
    week7 = models.CharField(max_length=150,null=True)
    week8 = models.CharField(max_length=150,null=True)
    week9 = models.CharField(max_length=150,null=True)
    week10 = models.CharField(max_length=150,null=True)
    week11 = models.CharField(max_length=150,null=True)
    week12 = models.CharField(max_length=150,null=True)
    week13 = models.CharField(max_length=150,null=True)
    week14 = models.CharField(max_length=150,null=True)
    week15 = models.CharField(max_length=150,null=True)
    week16 = models.CharField(max_length=150,null=True)
    week17 = models.CharField(max_length=150,null=True)
    week18 = models.CharField(max_length=150,null=True)
    week19 = models.CharField(max_length=150,null=True)
    week20 = models.CharField(max_length=150,null=True)
    week21 = models.CharField(max_length=150,null=True)
    week22 = models.CharField(max_length=150,null=True)
    week23 = models.CharField(max_length=150,null=True)
    week24 = models.CharField(max_length=150,null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE,null=True)