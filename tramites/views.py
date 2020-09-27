from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic import CreateView
from django.views import View
from django.urls import reverse
from .forms import TramiteForm, ConsultarTramiteForm
from django.views.generic import *
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import get_template
import random
import datetime
from django.contrib import messages


def send_user_mail(nombre, email, numero_solicitud, fecha_solucion, tipo_tramite):
    subject = 'Registro de rádicado en Konexbvc'
    template = get_template('email_content.html')
    content = template.render({
        'nombre': nombre,
        'tipo_solicitud': tipo_tramite,
        'fecha_respuesta': fecha_solucion,
        'numero_solicitud': numero_solicitud,
    })
    message = EmailMultiAlternatives(subject, #Titulo
                                    '',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [email]) #Destinatario

    message.attach_alternative(content, 'text/html')
    message.send()



def index(request):
    return render(request, 'tramites/index.html')


def detalleTramite(request):
    model = Tramite
    context = {}
    numero_tramite = request.POST.get('numero_tramite', None)

    try:
        if numero_tramite is not None and numero_tramite is not '' and int(numero_tramite):
            tramite = Tramite.objects.get(pk=int(numero_tramite))

            areas = ['Soporte TI', 'Documento Electrónico', 'Soporte Nivel 3', 'Ofimatica', 'Equipo Comercial']
            area_encargada = random.choice(areas)

            id_estado = random.choice(range(5))
            estados = ['Registrado', 'Asignado a un asesor', 'En proceso', 'Cumplimiento y calidad', 'Solucionado']

            estado = estados[id_estado - 1]

            context['numero_tramite'] = numero_tramite
            context['tramite'] = tramite
            context['area_encargada'] = area_encargada
            context['estado'] = estado
            context['id_estado'] = id_estado
            context['dias_solucion'] = 7 - id_estado
            context['fecha_solucion'] = tramite.fecha_registro + datetime.timedelta(days=7)

            return render(request, 'tramites/consultarTramite.html', context)

        else:
            messages.add_message(request, messages.WARNING, 'Debe ingresar un valor númerico')
            return render(request, 'tramites/index.html')
    except (Tramite.DoesNotExist, ValueError):
        messages.add_message(request, messages.WARNING, 'Debe ingresar un valor númerico')
        return render(request, 'tramites/index.html')



class IndexView(FormView):
    template_name = 'tramites/index.html'
    context_object_name = 'mensaje'
    form_class = ConsultarTramiteForm
    success_url = '/tramites/detalle_tramite'


    #queryset = Personaje.objects.all()
    #serializer_class = DeporteSerializer

    def get_queryset(self):
        return "Pagina inicial"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TramitesView(CreateView):
    model = Tramite
    template_name = "tramites/registrarTramite.html"
    form_class = TramiteForm
    success_url = '/tramites/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        tramite = form.save()

        send_user_mail(tramite.nombre, tramite.correo, tramite.id, tramite.fecha_registro + datetime.timedelta(days=7), Tramite.TRAMITES_CHOICES[Tramite.tramite])
        messages.info(self.request, 'Tu trámite ha sido registrsdo satisfactoriamente! Trámite No. ' + str(tramite.id))
        return super().form_valid(form)


class ConsultarTramiteView(FormView):
    form_class = ConsultarTramiteForm
    template_name = "tramites/index.html"
    #success_url = reverse('Konexbvc:consultar_tramite')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DetalleTramiteView(ListView):
    template_name = "tramites/consultarTramite.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
