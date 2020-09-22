from rest_framework import viewsets
from . import models, serializers
from django.db.models.signals import pre_save
from rest_framework.permissions import IsAuthenticated


class UserDetailsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserDetailsSerializer
    queryset = models.CustomUser.objects.all()

# moved user verification view from main to account cause it is concerned with the account


class UserVerificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserVerificationSerializer
    queryset = models.UserVerification.objects.all()


# signal to verify user when a UserVerificaton model instance is saved
def verify_user(sender, instance, **kwargs):
    if not sender.objects.filter(id=instance.id).exists():
        user = instance.user
        user.is_verified = True
        user.save()


pre_save.connect(receiver=verify_user,
                 sender=models.UserVerification, dispatch_uid='verify_user')
