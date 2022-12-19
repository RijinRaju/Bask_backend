from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,phone,img,DOB, domain_name=None,password=None):
        if not email:
            raise ValueError("User  must have an email ")

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
            phone = phone,
            img = img,
            DOB = DOB,
            domain_name = domain_name


        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name=None, last_name=None,phone=None,img=None,DOB=None,domain_name=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            phone = phone,
            DOB = DOB,
            img = img,
            domain_name = domain_name

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Domain(models.Model):
    img = models.FileField(upload_to='Frontend/src/Assests/Domains',verbose_name='domain image')
    title = models.CharField(max_length=150,null=False)





class Users(AbstractBaseUser):
    first_name = models.CharField(max_length=150,null=True)
    last_name = models.CharField(max_length=150,null=True)
    email = models.CharField(max_length=150,null=True,unique=True)
    phone = models.CharField(max_length=150,null=True)
    img = models.FileField(upload_to='Frontend/src/Assests/Advisors',verbose_name="advisor images",null=True)
    role = models.CharField(max_length=150,default='Advisor')
    status = models.BooleanField(default=True)
    DOB = models.DateField(null=True)
    password = models.CharField(max_length=150,null=True)
    domain_name = models.ForeignKey(Domain,on_delete = models.CASCADE,null=True)
    Date_of_joining = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class Batch(models.Model):
    Batch_name = models.CharField(max_length=150,null=True)
    location = models.CharField(max_length=150,null=True)
    batch_advisor = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=True)
    batch_status = models.BooleanField(default=True)


class Task(models.Model):
    advisor = models.ForeignKey(Users, on_delete=models.CASCADE,null=True)
    Batch = models.ForeignKey(Batch,on_delete= models.CASCADE,null=True)
    domain = models.ForeignKey(Domain,on_delete=models.CASCADE,null=True)
    task = models.JSONField(null=True)
    week = models.CharField(max_length=150,null=True)
    date = models.DateField(auto_now=True)