from functools import partial
from importlib.metadata import requires
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from Admin.models import Users
from Admin.serializers import AdvisorsSerializers
from .serializers import ProfileSerializers, SignupSerializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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
    domain = data.get('domain_name',None)
    print(domain)
    if Users.objects.filter(email=email).exists():
        return Response(status= status.HTTP_208_ALREADY_REPORTED)
    serializer = SignupSerializers(data = request.data,partial=True)
    
    if serializer.is_valid():
        serializer.save()
        student = Users.objects.get(email=email)
        student.role = "Student"
        student.save() 
       
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
        stu_token, _ = Token.objects.get_or_create(user=student_token)
        return Response({'studentToken':str(stu_token)})
    else:
        return Response({'msg':"user not exists"})


@api_view(['POST'])
def profile(request):
    id = request.data.get('id',None)
    print(id)
    student = Users.objects.get(id=id)
    serializers = ProfileSerializers(student)

    return Response(serializers.data)


@api_view(['POST'])
def profile_update(request):

    return Response("data received")