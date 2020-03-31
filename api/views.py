from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TemplateSerializer, UserSerializer, EffectSerializer
from .models import Template, User, Effect


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EffectViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer