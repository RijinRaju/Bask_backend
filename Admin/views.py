from functools import partial
import imp
from socket import AddressInfo
from django.shortcuts import render
from rest_framework import status
from .models import  Batch, Domain, Task, Users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view,permission_classes,authentication_classes

from .serializers import  BatchSerializers, BatchSerializersRead, DomainSerializers,AdvisorsSerializers,TaskSerializers, TaskViewSerializers
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from Admin import serializers
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
def admin_login(request):
    data = request.data
    email = data.get('email',None)
    password = data.get('password',None)
    admin = authenticate(email=email,password=password)
    if admin:
        admin_token = Users.objects.get(email=email)
        token_obj, _ = Token.objects.get_or_create(user=admin_token)
        print(token_obj)
        return Response({"token" : str(token_obj)})
    else:
        return Response("errors")


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def domain(request):
    domains = Domain.objects.all()
    print(request.auth)
    serializers = DomainSerializers(domains, many=True)
    return Response(serializers.data)


@api_view(['POST','GET'])
def add_domain(request):
    data = request.data
    title = data.get('title',None)   
    domain  = Domain.objects.filter(title__icontains=title).exists()
    if domain:
        return Response(status= status.HTTP_403_FORBIDDEN)    
    serializer = DomainSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        domains = Domain.objects.all()
        domainList= DomainSerializers(domains,many=True)
        return Response(domainList.data)
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_advisors(request):
    data = request.data
    print(data)
    email = request.POST.getlist('email')
    # email = data.get('email')
    print(data.get('email'))

    if Users.objects.filter(email=data.get('email')).exists():
        return Response("Email already taken")
    else:
        serializer = AdvisorsSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()

            # sending email to the new advisors to inform password for login
            message = "Hi ,welcome to our family your account PASSWORD: "+data.get('password')+" for EMAIL:  "+data.get('email')
            subject  = "welcome mail"

            send_mail(
                subject,
                message,
                'b@gmail.com',
                email,
                fail_silently=False,

            )
            return Response("data saved")
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def list_advisors(request):
    adv = Users.objects.filter(is_admin = False,role = "Advisor")
    serializer = AdvisorsSerializers(adv, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def remove_advisors(request):
    data = request.data
    id = data.get('id',None)
    Users.objects.filter(id=id).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def batch_list(request):
    lst = Batch.objects.all()
    serializer = BatchSerializersRead(lst,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_batch(request):
    data = request.data
    print(data)
    serializer = BatchSerializers(data = data)
    if serializer.is_valid():
        serializer.save()
        bch_list = Batch.objects.all()
        batchSerializer = BatchSerializers(bch_list,many=True)
        return Response(batchSerializer.data)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
def add_task(request):
    
    seralizer = TaskSerializers(data=request.data,partial=True)
    if seralizer.is_valid():
        seralizer.save()
        return Response("data saved")
    return Response('error')


@api_view(['POST'])
def task_view(request):
    task = Task.objects.all()
    serializers = TaskViewSerializers(task, many=True)
    return Response(serializers.data)