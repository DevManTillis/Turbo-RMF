from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.forms import modelformset_factory
from django.core import serializers

from theform.models import *
from theform.serializers import VulnSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer

from django.contrib.auth.models import User

from upload.models import *


###


def index(request):
    crap = "Hello World!"
    return render(request, 'theform/index.html', {'crap': crap})


# RETURN ANGULAR FORM
def vulns(request,pk):
    #crap = pk
    return render(request, 'theform/index_vulns.html', {'pk': pk})

# REST API OF VULN LIST
@api_view(['GET', 'POST'])
def VulnList(request,pk):
    try:
        query = Checklist.objects.get(pk=pk)
        queryset = query.vuln_set.all()
    except queryset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VulnSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VulnSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'DELETE':
#        queryset.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

"""
class VulnList(generics.ListCreateAPIView):
    queryset = Vuln.objects.filter(checklist__id=1)
    serializer_class = VulnSerializer
"""

class VulnDetail(generics.RetrieveUpdateDestroyAPIView):
    #cid = ""
    queryset = Vuln.objects.all()
    serializer_class = VulnSerializer


class ListChecklists(generic.ListView):
    model = Checklist
    template_name = 'theform/list.html'
    context_object_name = 'checklist'

    def get_queryset(self):
        """Return the last five published questions."""
        return Checklist.objects.all()


