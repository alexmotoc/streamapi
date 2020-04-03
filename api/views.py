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


procs = []
FNULL = open(os.devnull, 'w')


@api_view(['POST'])
def start_stream(request):
    if request.method == 'POST':
        stream_key = request.POST.get('name')
        existing_streams = Stream.objects.filter(stream_key=stream_key)
        existing_streams.delete()

        tokens = json.loads(str(User.objects.all()[0]))
        twitch_stream_key = tokens.get('twitch').get('streamKey')

        pid1 = subprocess.Popen('/home/alex/RngStreaming/build_rel/cmd/simple-backend ' + str(stream_key), close_fds=True, shell=True, stdout=FNULL, preexec_fn=os.setsid)
        pid2 = subprocess.Popen('/bin/bash /home/alex/RngStreaming/outputs/twitch.sh ' + str(stream_key) + ' ' + str(twitch_stream_key), close_fds=True, shell=True, cwd='/home/alex/RngStreaming/outputs/', preexec_fn=os.setsid)
        
        # Add to global list so they aren't automatically killed
        global procs
        procs.append(pid1)
        procs.append(pid2)

        new_stream = Stream.objects.create(stream_key=stream_key, process_ids='{},{}'.format(str(os.getpgid(pid1.pid)), str(os.getpgid(pid2.pid))))

        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def stop_stream(request):
    if request.method == 'POST':
        stream_key = request.POST.get('name')

        stream = Stream.objects.filter(stream_key=stream_key)[0]

        for pid in stream.process_ids.split(','):
            os.killpg(int(pid), signal.SIGTERM)

        #stream.delete()

        return Response(status=status.HTTP_200_OK)
