from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarTramite', views.TramitesView, name='registrar_tramite'),
]