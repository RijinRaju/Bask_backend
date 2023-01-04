from dataclasses import field
from rest_framework import serializers
from Admin.models import Manifest



class ManifestUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manifest
        fields = '__all__'


class ManifestViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manifest
        fields = '__all__'
        depth = 1
        