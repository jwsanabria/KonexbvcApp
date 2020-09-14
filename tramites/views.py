from django.http import HttpResponse
from .models import *
from django.views.generic import CreateView
from django.urls import reverse
from .forms import TramiteForm
from django.views.generic import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(ListView):
    template_name = 'tramites/index.html'
    context_object_name = 'mensaje'
    #queryset = Personaje.objects.all()
    #serializer_class = DeporteSerializer

    def get_queryset(self):
        return "Pagina inicial"


class TramitesView(CreateView):
    model = Tramite
    template_name = "tramites/registrarTramite.html"
    form_class = TramiteForm
    #success_url = reverse('Konexbvc:index')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TramitesView, self).form_valid(form)