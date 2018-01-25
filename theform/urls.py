from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'theform'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vulns/$', views.vulns, name='vulns'),
    #
    url(r'^vulns/map/$', views.map, name='map'),
    url(r'^vulns/main/$', views.main, name='main'),
    url(r'^vulns/low/$', views.low, name='low'),
    url(r'^vulns/medium/$', views.medium, name='medium'),
    url(r'^vulns/high/$', views.high, name='high'),
    #
    url(r'^vuln/$', views.VulnList.as_view()),
    url(r'^vuln/(?P<pk>[0-9]+)/$', views.VulnDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
