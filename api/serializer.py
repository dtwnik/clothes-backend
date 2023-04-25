from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class MenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Men
        fields = '__all__'


class WomanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Woman
        fields = '__all__'


class KidsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kids
        fields = '__all__'


class BestsellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bestseller
        fields = '__all__'

