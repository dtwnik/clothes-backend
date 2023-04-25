
from rest_framework import viewsets
from .serializer import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user_id=response.data["id"])
        response.data["token"] = str(token)
        return response


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class MenViewSet(viewsets.ModelViewSet):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['season']


class WomanViewSet(viewsets.ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['season']


class KidsViewSet(viewsets.ModelViewSet):
    queryset = Kids.objects.all()
    serializer_class = KidsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['season']


class BestsellerViewSet(viewsets.ModelViewSet):
    queryset = Bestseller.objects.all()
    serializer_class = BestsellerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['season']