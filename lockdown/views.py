from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
#from theform.forms import *
from django.forms import modelformset_factory
from theform.models import *
from upload.models import *
import copy
from .pywinrm import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse

from .forms import NameForm


from lockdown.models import *
from lockdown.serializers import CommandSerializer

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
import json

# Create your views here.

# STANDARD INDEX HELLO WORLD! APPLICATION
"""
def index(request):
    #form = "Hello World!"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            host_name = form.cleaned_data['host_name']
            admin_username = form.cleaned_data['admin_username']
            admin_password = form.cleaned_data['admin_password']
            command = form.cleaned_data['command']
            u_initiate = remote_command(host_name, admin_username, admin_password, command)
            raw = u_initiate
            initiate = "<br/>".join(raw.split("\n"))
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            return render(request, 'lockdown/index.html', {'form': form, 'initiate':initiate})
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'lockdown/index.html', {'form': form})
    #return render(request, 'theform/index.html', {'form': form})
"""

def index(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    template_name = 'lockdown/index.html'
    return Response({"message": "Hello, world!"})

class CommandList(generics.ListCreateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer


class CommandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

# tfweb499
# encinitas flowers

class SignUpView(CreateView):
    template_name = 'lockdown/signup.html'
    form_class = UserCreationForm

def RunCommand(request):
    json_data = json.loads(request.body)
    u_initiate = remote_command(
        json_data.get("ip_addr"),
        json_data.get('admin_username'),
        json_data.get('admin_password'),
        json_data.get('command')
        )
    return JsonResponse(u_initiate, safe=False)



    
