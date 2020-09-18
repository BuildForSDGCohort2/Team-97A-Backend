from rest_framework import generics, viewsets
from . import models, serializers

class UserDetailsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserDetailsSerializer
    queryset = models.CustomUser.objects.all()