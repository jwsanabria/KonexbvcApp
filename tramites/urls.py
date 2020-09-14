from django.conf.urls import url, include

from . import views

app_name = 'Konexbvc'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^registrarTramite$', views.TramitesView.as_view(), name='registrar_tramite'),
]