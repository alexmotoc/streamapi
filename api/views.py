from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TemplateSerializer, UserSerializer
from .models import Template, User


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer