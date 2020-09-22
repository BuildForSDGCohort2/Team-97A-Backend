from rest_framework.serializers import ModelSerializer
from . import models


class TrackerSerializer(ModelSerializer):
    class Meta:
        model = models.Tracker
        fields = '__all__'


class PackageSerializer(ModelSerializer):
    tracker = TrackerSerializer(read_only=True)

    class Meta:
        model = models.Package
        fields = '__all__'
