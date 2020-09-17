from django.conf.urls import url, include

from . import views

app_name = 'Konexbvc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrarTramite$', views.TramitesView.as_view(), name='registrar_tramite'),
    url(r'^consultarTramite$', views.ConsultarTramiteView.as_view(), name='consultar_tramite'),
    url(r'^detalleTramite$', views.detalleTramite, name='detalle_tramite'),
]