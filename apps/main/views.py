from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.db.models.signals import pre_save
from rest_framework import viewsets
from . import serializers, models
import random
import string


class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello Dashboad!'}
        return Response(content)


class PackageViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PackageSerializer
    queryset = models.Package.objects.all()


class TrackerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.TrackerSerializer
    queryset = models.Tracker.objects.all()


# signal to initialize a new tracker anythime the a package instance is saved
def create_package_tracker(sender, instance, **kwargs):
    if not sender.objects.filter(id=instance.id).exists():
        pin=generate_pin()
        instance.security_code=pin
        tracker = models.Tracker(is_confirmed=False)
        tracker.save()
        instance.tracker = tracker


pre_save.connect(receiver=create_package_tracker,
                 sender=models.Package, dispatch_uid='create_package_tracker')

#generates pin for each new package being added
def generate_pin():
    digits=string.digits
    pin = ''.join(random.choice(digits) for i in range(5))
    return pin