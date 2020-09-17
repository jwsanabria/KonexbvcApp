from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic import CreateView
from django.views import View
from django.urls import reverse
from .forms import TramiteForm, ConsultarTramiteForm
from django.views.generic import *
from django.views.generic.edit import FormView
from django.shortcuts import render

def index(request):
    return render(request, 'tramites/index.html')


def detalleTramite(request):
    context = {}
    numero_tramite = request.POST.get('numero_tramite', None)
    context['numero_tramite'] = numero_tramite
    return render(request, 'tramites/consultarTramite.html', context)


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
    #success_url = reverse('Konexbvc:index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TramitesView, self).form_valid(form)


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
