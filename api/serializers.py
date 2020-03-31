from rest_framework import serializers

from .models import Template, User, Effect

class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EffectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Effect
        fields = "__all__"