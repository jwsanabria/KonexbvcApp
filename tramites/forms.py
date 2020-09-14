from django import forms
from .models import Tramite

class TramiteForm(forms.ModelForm):
    class Meta:
        model = Tramite

        fields = [
            'nombre',
            'correo',
            'tramite',
            'comunicacion',
            'solicitud',
        ]
        labels = {
            'nombre': 'Nombres',
            'correo': 'Correo',
            'tramite': 'Trámite',
            'comunicacion': 'Preferencia Comunicación',
            'solicitud': 'Solicitud',
        }
        widgets = {

        }