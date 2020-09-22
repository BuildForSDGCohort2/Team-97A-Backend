from rest_framework.serializers import ModelSerializer
from . import models


class TrackerSerializer(ModelSerializer):
    class Meta:
        model = models.Tracker
        fields = '__all__'


class PackageSerializer(ModelSerializer):

    class Meta:
        model = models.Package
        fields = '__all__'
        # fields = ('name', 'weight', 'category', 'price', 'pick_location', 'dest_location',
        #   'delivered_on', 'description', 'owner', 'carrier', 'tracker')


class PackageSerializerDetails(ModelSerializer):
    tracker = TrackerSerializer(read_only=True)

    class Meta:
        model = models.Package
        fields = '__all__'
