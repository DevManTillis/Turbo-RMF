from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'theform'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vulns/$', views.vulns, name='vulns'),
    # pass id to vulns
    url(r'^vulns/(?P<pk>[0-9]+)/$', views.vulns, name='vulns'),
    #
    url(r'^checklist/(?P<pk>[0-9]+)/$', views.VulnList, name="checklist"),
    url(r'^vuln/(?P<pk>[0-9]+)/$', views.VulnDetail.as_view()),
    #ListChecklists
    url(r'^checklists/$', views.ListChecklists.as_view(), name="checklists"),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
