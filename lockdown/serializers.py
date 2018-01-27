from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from lockdown.models import *


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = (
            'v_command',
            #'v_command_status',
            #'v_command_enabled',
            )
