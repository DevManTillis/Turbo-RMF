from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

#from .models import Document
from upload.models import Checklist, Vuln
from .forms import DocumentForm
from django.utils import timezone
from .parse_xml import *


# Create your views here.
# process_xml("win10.ckl")[0]["vulnid"]

def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        context = "Authenticated!"
        return render(request, 'upload/index.html', {'context': context})
    else:
        # Do something for anonymous users.
        context = "Sorry NOT Authed!"
        return render(request, 'upload/index.html', {'context': context})


# FILE UPLOAD
def run(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # PROCESS UPLOADED FILE
        # process_file(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        myfile.seek(0)
        # uploaded_file_url = fs.url(filename)
        # declare empty byte string
        data = b''
        chunks = myfile.chunks(chunk_size=None)
        for chunk in chunks:
            data += chunk
        # change byte file to UTF-8
        doc_data = str(data.decode(encoding='utf-8'))
        doc_name = str(myfile.name)
        doc_owner = str(request.user)
        c = Checklist(checklist_text=doc_name,checklist_owner=doc_owner, pub_date=timezone.now())
        c.save()
        # get private key

        sqlrow = Checklist.objects.get(pk=c.id)

        checklist_doc = process_xml(doc_data)
        for vuln in checklist_doc:
            sqlrow.vuln_set.create(
            v_ids = str(vuln["vulnid"]),vuln_text = str(vuln["vulnid"]),
            v_sev = str(vuln["severity"]),
            v_dis = str(vuln["vulndiscuss"]),
            v_con = str(vuln["checkcontent"]),
            v_fix = str(vuln["fixtext"]),
            v_ref = str(vuln["stigref"]),
            v_sta = str(vuln["status"]),
            v_com = str(vuln["comments"]),
            v_det = str(vuln["finding_details"])
                )
        
            
## q = Checklist.objects.get(pk=1)
## q.vuln_set.create(choice_text='Not much', votes=0)
        
        #database_add = Document(document_name=doc_name,document_owner=doc_owner,document_data=doc_data)
        #database_add.save()
        
        #documents = Document.objects.all()
        return render(request, 'upload/simple_upload.html', {
#            'uploaded_file_url': uploaded_file_url,
            'doc_data': doc_data,
            'doc_name': doc_name,
            'doc_owner': doc_owner
        })
    return render(request, 'upload/simple_upload.html')

def xml(request):
    return render(request, 'upload/test.html')


"""
def scanit():
    path = os.path.abspath('.\\vulnscan\VulnScan.ps1')
    #print(path)
    subprocess.Popen("cmd.exe")
    return str("bingo")
"""


"""
def run(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        
        context = scanit()
        return render(request, 'upload/run.html', {'context': context})
    else:
        # Do something for anonymous users.
        context = "Sorry NOT Authed!"
        return render(request, 'upload/run.html', {'context': context})


def run(request):
    documents = Document.objects.all()
    return render(request, 'upload/home.html', { 'documents': documents })
"""

