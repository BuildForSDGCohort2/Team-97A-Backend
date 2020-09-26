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


