from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.db.models.signals import pre_save
from rest_framework import viewsets
from . import serializers, models


class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello Dashboad!'}
        return Response(content)


class PackageViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PackageSerializerDetails
    queryset = models.Package.objects.all()

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = serializers.PackageSerializerDetails
        if not request.user.is_staff:
            self.queryset = self.queryset.filter(user=request.user.id)
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # to update tracker
        tracker_id = request.data['tracker']['id']
        tracker = get_object_or_404(models.Tracker, id=tracker_id)
        is_uploaded = request.data['tracker']['is_uploaded']
        in_transit = request.data['tracker']['in_transit']
        is_delivered = request.data['tracker']['is_delivered']
        tracker.is_delivered = is_delivered
        tracker.in_transit = in_transit
        tracker.is_uploaded = is_uploaded
        tracker.save()
        print(tracker)

        return super().update(request, *args, **kwargs)


class TrackerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.TrackerSerializer
    queryset = models.Tracker.objects.all()


# signal to initialize a new model anythime the a package instance is saved
def create_package_tracker(sender, instance, **kwargs):
    if not sender.objects.filter(id=instance.id).exists():
        tracker = models.Tracker(is_uploaded=True)
        tracker.save()
        instance.tracker = tracker


pre_save.connect(receiver=create_package_tracker,
                 sender=models.Package, dispatch_uid='create_package_tracker')
