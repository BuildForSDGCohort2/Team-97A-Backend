from rest_framework.serializers import ModelSerializer
from . import models


class TrackerSerializer(ModelSerializer):
    class Meta:
        model = models.Tracker
        fields = '__all__'


class PackageSerializer(ModelSerializer):
    tracker = TrackerSerializer(read_only=True)

    class Meta:
        model = models.Package
        fields = '__all__'


# serializers for wallet and transaction models 

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ['running_balance', 'amount', 'is_credit', 'created_at']


class WalletSerializer(ModelSerializer):
    transactions=TransactionSerializer(many=True, read_only=True)
    class Meta:
        model = models.Wallet
        fields = ['id', 'user', 'current_balance', 'transactions']