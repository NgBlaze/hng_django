from cProfile import label
from dataclasses import fields
from rest_framework import serializers
from .models import SlackUser



class SlackUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackUser
        fields = ['id', 'slackUsername', 'backend', 'age', 'bio']