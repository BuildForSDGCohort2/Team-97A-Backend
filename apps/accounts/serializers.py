from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from . import models

# custom registration serializer


class RegistrationSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.phone_number = self.validated_data.get('phone_number', '')
        user.address = self.validated_data.get('address', '')
        user.save(update_fields=['first_name',
                                 'last_name', 'phone_number', 'address'])


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'first_name', 'last_name',
                  'phone_number', 'address', 'is_verified')


# moved user verification serializers from main to accounts cause it is concerned with the accounts and user section
class UserVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserVerification
        fields = '__all__'
