from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from upload.models import *


class VulnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuln
        fields = (
            'v_ids',
            'v_sev',
            'v_sta',
            'v_dis',
            'v_con',
            'v_fix',
            'v_command',
            #'v_command_status',
            #'v_command_enabled',
            'Comments',
            'Finding_Details',
            'id',
            #'Finding_Details',
            #'v_ref',
            #'v_sta',
            #'Comments',
            #'v_det',
            )


"""
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    v_ids = models.CharField(max_length=200,default='NONE')
    vuln_text = models.CharField(max_length=200,default='NONE')

    #v_sev = models.CharField(max_length=200,default='NONE')
    v_sev = models.CharField(max_length=200,default='NONE')
    v_dis = models.CharField(max_length=900,default='NONE')
    v_con = models.CharField(max_length=900,default='NONE')
    v_fix = models.CharField(max_length=900,default='NONE')
    Finding_Details = models.CharField(max_length=200,default='NONE')
    v_ref = models.CharField(max_length=200,default='NONE')
    v_sta = models.CharField(max_length=200,default='NONE')
    Comments = models.CharField(max_length=200,default='NONE')
    v_det = models.CharField(max_length=200,default='NONE')
#   v_det = models.CharField(max_length=200, default='NONE')
"""
