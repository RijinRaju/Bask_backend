from copyreg import constructor
from functools import partial
from importlib.metadata import requires
from telnetlib import DO
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from Admin.models import Allocate, Task, Users,Domain
from Admin.serializers import  DomainSerializers, TaskSerializers
from .serializers import ProfileSerializers, ProfileUpdateSerializers, SignupSerializers, TaskViewSerializers,BatchSerializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail
from Students import serializers
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['first_name'] = user.first_name
        token['email'] = user.email

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def signUp(request):
    data  = request.data
    email = data.get('email',None)
    toEmail = request.data.get('email',None)
    if Users.objects.filter(email=email).exists():
        return Response(status= status.HTTP_208_ALREADY_REPORTED)
    serializer = SignupSerializers(data = request.data,partial=True)
    
    if serializer.is_valid():
        serializer.save()
        student = Users.objects.get(email=email)
        student.role = "Student"
        student.save() 
        # sending email to the new advisors to inform password for login
        message = "we got the request to signin .Your account will be activated after varifiaction. THANK YOU "
        subject = "confirmation mail"

        send_mail(
            subject,
            message,
            'b@gmail.com',
            [toEmail],
            fail_silently=False,

        )
        return Response("user created")
    else:
        print("errors in python",serializer.errors)
        return Response(serializer.errors)


@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email',None)
    password = data.get('password',None)
    student = authenticate(email=email,password=password)
    if student:
        student_token = Users.objects.get(email=email)
        print(student_token.is_admin)
        if student_token.is_admin == False:
            stu_token, _ = Token.objects.get_or_create(user=student_token)
            return Response({'studentToken':str(stu_token)})
    else:
        return Response({'msg':"user not exists"})


@api_view(['POST'])
def profile(request):
    id = request.data.get('id',None)
    student = Users.objects.get(id=id)
    batch = Allocate.objects.get(student=id)
    serializers = ProfileSerializers(student)
    batchSerializer = BatchSerializers(batch)
    return Response({'profile':serializers.data,'batch':batchSerializer.data})

@api_view(['GET'])
def domains(request):
    domain = Domain.objects.all()
    serializer = DomainSerializers(domain,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def profile_update(request):
    id = request.data.get('id',None)
    domain = request.data.get('domain_name',None)
    img  = request.data.get('img',None)
    user = Users.objects.get(id=id)
    dm = Domain.objects.get(id=domain)
    user.img = img
    user.domain_name = dm
    user.save()
    return Response("no error")


@api_view(['POST'])
def task_view(request):
    id = request.data.get('id',None)
    print(id)
    student = Users.objects.get(id=id)
    domain_id = student.domain_name.id
    task = Task.objects.filter(domain=domain_id)
    serializers = TaskViewSerializers(task,many=True)
    return Response(serializers.data)


@api_view(['POST'])
def del_task(request):
    id = request.data.get('id',None)
    tsk = Task.objects.get(id=id).delete()
    serializers = TaskSerializers(tsk)
    return Response(serializers.data)

def chat(request):
    return render(request, "students/chat.html")


def room(request, room_name):
    return render(request, "students/room.html", {"room_name": room_name})
