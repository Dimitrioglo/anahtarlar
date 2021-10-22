from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Key, Product, SoldDateList, UserExtended


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = []


class KeySerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Key
        exclude = []


class SoldDateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldDateList
        fields = [
            'created_by',
            'created_date',
            'key'
        ]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserExtendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtended
        fields = '__all__'
