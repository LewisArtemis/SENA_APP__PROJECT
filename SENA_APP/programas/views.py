from django.http import HttpResponse
from django.template import loader
from .models import Programa
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from programas.forms import ProgramaForm
from django.views import generic
from django.contrib import messages
from django.views.generic import FormView

# Create your views here.

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')
    context = {
    'lista_programas': lista_programas,
    'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id= programa_id)
    cursos = programa.curso_set.all().order_by('-fecha_inicio')
    template = loader.get_template('detalle_programa.html')
    
    context = {
        'programa': programa,
        'cursos': cursos,
    }
    return HttpResponse(template.render(context, request))

class ProgramaFormView(generic.FormView):
    template_name = 'crear_programa.html'
    form_class = ProgramaForm
    success_url = '../programas/'
    
    #metodo para guardar el formulario
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
