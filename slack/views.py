from turtle import title
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.


class SlackApiView(generics.ListCreateAPIView):
        queryset = SlackUser.objects.all()
        serializer_class = SlackUserSerializer