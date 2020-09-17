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
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'tramite': forms.Select(attrs={'class':'form-control'}),
            'comunicacion': forms.Select(attrs={'class':'form-control'}),
            'solicitud': forms.Textarea(attrs={'class':'form-control'}),
        }


class ConsultarTramiteForm(forms.Form):
    numero_tramite = forms.CharField()
    #message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass