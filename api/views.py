from django.shortcuts import render
from rest_framework import viewsets

from .serializers import OverlaySerializer
from .models import Overlay


class OverlayViewSet(viewsets.ModelViewSet):
    queryset = Overlay.objects.all()
    serializer_class = OverlaySerializer