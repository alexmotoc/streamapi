import json
import os
import signal
import subprocess

from django.shortcuts import render
from rest_framework import viewsets

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TemplateSerializer, UserSerializer, EffectSerializer
from .models import Template, User, Effect, Stream


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EffectViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer


@api_view(['POST'])
def start_stream(request):
    if request.method == 'POST':
        stream_key = request.POST.get('name')

        tokens = json.loads(str(User.objects.all()[0]))
        twitch_stream_key = tokens.get('twitch').get('streamKey')

        pid1 = subprocess.Popen(['~/RngStreaming/build/cmd/simple-backend', stream_key])
        pid2 = subprocess.Popen(['~/RngStreaming/outputs/twitch', stream_key, twitch_stream_key])

        new_stream = Stream.objects.create(stream_key=stream_key, process_ids='{}, {}'.format(str(pid1), str(pid2)))
        new_stream.save()

        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def stop_stream(request):
    if request.method == 'POST':
        stream_key = request.POST.get('name')

        stream = Stream.objects.filter(stream_key=stream_key)[0]

        for pid in stream.process_ids.split(', '):            
            os.kill(int(pid), signal.SIGTERM)

        stream.delete()

        return Response(status=status.HTTP_200_OK)
