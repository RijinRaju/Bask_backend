from functools import partial
from Admin.models import Allocate,Manifest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Admin.serializers import StudentsListSerializers
from Advisors import serializers
from Advisors.serializers import ManifestUpdateSerializers, ManifestViewSerializers
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
    print(serializer.data)
    if not serializer:
        return Response("updates")
    return Response(serializer.data)


@api_view(['POST'])
def update_manifest(request):
    week = request.data.get('week',None)
    user = request.data.get('user',None)
    print(week ,user)
    if Manifest.objects.filter(week=week,user=user).exists():
        mnfst = Manifest.objects.get(week=week,user=user)
        updateSerializers = ManifestUpdateSerializers(mnfst,data=request.data,partial=True)
        if updateSerializers.is_valid():
            updateSerializers.save() 
            mnfst = Manifest.objects.filter(week=week, user=user)
            print(mnfst)
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
    