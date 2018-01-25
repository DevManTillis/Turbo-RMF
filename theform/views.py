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

def map(request):
    crap = "Hello World!"
    return render(request, 'theform/map.html', {'crap': crap})

def main(request):
    crap = "Hello World!"
    return render(request, 'theform/main.html', {'crap': crap})

def low(request):
    crap = "Hello World!"
    return render(request, 'theform/low.html', {'crap': crap})

def medium(request):
    crap = "Hello World!"
    return render(request, 'theform/medium.html', {'crap': crap})

def high(request):
    crap = "Hello World!"
    return render(request, 'theform/high.html', {'crap': crap})




def vulns(request):
    crap = "Hello World!"
    return render(request, 'theform/index_vulns.html', {'crap': crap})


class VulnList(generics.ListCreateAPIView):
    queryset = Vuln.objects.all()
    serializer_class = VulnSerializer


class VulnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vuln.objects.all()
    serializer_class = VulnSerializer





