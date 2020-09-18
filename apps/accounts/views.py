from rest_framework import generics, viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated

class UserDetailsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.UserDetailsSerializer
    queryset = models.CustomUser.objects.all()