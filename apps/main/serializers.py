from rest_framework.serializers import ModelSerializer
from . import models

class TrackerSerializer(ModelSerializer):
    class Meta:
        model = models.Tracker
        fields = '__all__'

class PackageSerializer(ModelSerializer):
    class Meta:
        model = models.Package
        fields = ('name', 'weight', 'category', 'price', 'pick_location', 'dest_location', 'delivered_on', 'description', 'owner', 'carrier')

class PackageSerializerDetails(ModelSerializer):
    tracker = TrackerSerializer()
    class Meta:
        model = models.Package
        fields = '__all__'

class PackageVerificationSerializer(ModelSerializer):
    class Meta:
        models = models.PackageVerification
        fields = '__all__'

class PackageVerificationSerializerDetails(ModelSerializer):
    class Meta:
        model = models.PackageVerification
        fields = '__all__'