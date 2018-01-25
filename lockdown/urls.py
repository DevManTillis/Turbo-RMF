from django.conf.urls import url
from . import views

app_name = 'lockdown'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^lockdown/validate_username/$', views.validate_username, name='validate_username'),
]
