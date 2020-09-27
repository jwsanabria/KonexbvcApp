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
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre'}),
            'correo': forms.EmailInput(attrs={'class':'form-control', 'aria-describedby':'emailHelp', 'placeholder':'Ingrese su email'}),
            'tramite': forms.Select(attrs={'class':'form-control', 'placeholder':'Tipo de trámite'}),
            'comunicacion': forms.Select(attrs={'class':'form-control', 'placeholder':'Medio de respuesta'}),
            'solicitud': forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese su solicitud', 'rows':10}),
        }


class ConsultarTramiteForm(forms.Form):
    numero_tramite = forms.IntegerField()
    #message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass