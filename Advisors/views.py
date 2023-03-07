from telnetlib import STATUS
from django.dispatch import receiver
from Admin.models import Allocate, Answers, Batch,Manifest
from Advisors.models import Reports
from Students.models import Messages,Room
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from Admin.serializers import StudentsListSerializers
from Advisors import serializers
from Advisors.serializers import BatchListSerializers, ChatListSerializers, ManifestUpdateSerializers, ManifestViewSerializers, RecordChatSerializers, ReportSerializers, VerifyTaskSerializers
# Create your views here.


@api_view(['POST'])
def students_manifest(request):
    id = request.data.get('id',None)
    advisor = request.data.get('user',None)
    students = Allocate.objects.filter(batch=id,advisor=advisor)
    print(students)
    serializers = StudentsListSerializers(students,many=True)
    return Response(serializers.data)



@api_view(['POST'])
def manifest(request):
    # week = request.data.get('week',None)
    user = request.data.get('user',None)
    manifest = Manifest.objects.filter(user=user)
    serializer = ManifestViewSerializers(manifest,many=True)
    if not serializer:
        return Response("updates")
    return Response(serializer.data)


@api_view(['POST'])
def update_manifest(request):
    week = request.data.get('week',None)
    user = request.data.get('user',None)
    if Manifest.objects.filter(week=week,user=user).exists():
        print("true")
        mnfst = Manifest.objects.get(week=week,user=user)
        updateSerializers = ManifestUpdateSerializers(mnfst,data=request.data,partial=True)
        if updateSerializers.is_valid():
            updateSerializers.save() 
            mnfst = Manifest.objects.filter(week=week, user=user)
            viewSerializer = ManifestUpdateSerializers(mnfst,many=True)
            return Response(viewSerializer.data)
        else:
            return Response(updateSerializers.errors)
    serializer = ManifestUpdateSerializers(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        mnfst = Manifest.objects.filter(week=week, user=user)
        viewSerializer = ManifestUpdateSerializers(mnfst,many=True)
        return Response(viewSerializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(['POST'])
def chat_list(request):
    id = request.data.get('id',None)
    list = Allocate.objects.filter(advisor=id)
    serializers = ChatListSerializers(list,many=True)
    return Response(serializers.data) 


@api_view(["POST"])
def chat_record(request):
    sender = request.data.get('sender',None)
    room_name = request.data.get('room_name',None)
    print("sender and room_name",sender,room_name)
    room = Room.objects.get(room_name=room_name)
    chats = Messages.objects.filter(room_name=room)
    serializers =  RecordChatSerializers(chats,many=True)
    return Response(serializers.data)

@api_view(["POST"])
def advisor_batch_list(request):
    user = request.data.get('user',None)  
    batchs = Batch.objects.filter(batch_advisor = user)
    serializers = BatchListSerializers(batchs,many=True)
    return Response(serializers.data)

@api_view(["POST"])
def batch_report(request):
    serializer = ReportSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        reports = Reports.objects.all()
        serializer2 = ReportSerializers(reports,many=True)
    return Response(serializer2.data)

@api_view(["POST"])
def list_reports(request):
    reports = Reports.objects.all()
    serializers = ReportSerializers(reports,many=True)
    return Response(serializers.data)


@api_view(['POST'])
def check_task(request):
    student = request.data.get('user',None)
    task = Answers.objects.filter(user=student)
    serializer = VerifyTaskSerializers(task,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def verify_task(request):
    id = request.data.get('task_id',None)
    try:
        answer = Answers.objects.get(id=id)
        answer.status = True
        answer.save()
        return Response(status=status.HTTP_200_OK)

    except:
        return Response(status=status.HTTP_204_NO_CONTENT)