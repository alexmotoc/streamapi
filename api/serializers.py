from rest_framework import serializers

from .models import Overlay

class OverlaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Overlay
        fields = "__all__"