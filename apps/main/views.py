from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets
from . import serializers, models


class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello Dashboad!'}
        return Response(content)

class PackageViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PackageSerializer
    queryset = models.Package.objects.all()

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = serializers.PackageSerializerDetails
        if not request.user.is_staff:
            self.queryset = self.queryset.filter(user=request.user.id)
        super().retrieve(request, *args, **kwargs)

class PackageVerificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PackageVerificationSerializer
    queryset = models.PackageVerification.objects.all()

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = serializers.PackageVerificationSerializerDetails
        if not request.user.is_staff:
            self.queryset = self.queryset.filter(user=request.user.pk)
        super().retrieve(request, *args, **kwargs)

class TrackerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated)
    serializer_class = serializers.TrackerSerializer
    queryset = models.Tracker.objects.all()