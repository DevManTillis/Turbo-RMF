from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'upload'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^run$', views.run, name='run'),
    url(r'^xml$', views.xml, name='xml'),
]

##if settings.DEBUG:
##    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
