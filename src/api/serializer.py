from rest_framework import serializers

from src.accounts.models import Profile, User
from src.administration.admins.models import (
    Purchase, Package
)


class OpenAISerializer(serializers.Serializer):
    text = serializers.CharField(max_length=10000, required=True)


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        exclude = ['updated_on']


class PurchaseSerializer(serializers.ModelSerializer):
    package = PackageSerializer(read_only=True, many=False)

    class Meta:
        model = Purchase
        fields = ['id', 'package', 'amount_total', 'amount_paid', 'tokens', 'payment_method', 'is_active', 'created_on']
        read_only_fields = [
            'id', 'amount_total', 'amount_paid', 'tokens', 'is_active', 'created_on'
        ]


class PurchaseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ['id', 'package', 'amount_total', 'amount_paid', 'tokens', 'payment_method', 'is_active', 'created_on']
        read_only_fields = [
            'id', 'amount_total', 'amount_paid', 'tokens', 'is_active', 'created_on'
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'profile_image', 'first_name', 'last_name', 'username', 'email', 'phone_number',
            'is_active', 'date_joined', 'last_login'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user', 'tokens_total', 'tokens_used', 'tokens_available'
        ]
