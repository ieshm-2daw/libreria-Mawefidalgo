from django.shortcuts import render
from .models import Libro
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
class Listado(ListView):

    model = Libro
    template_name = 'AppLibreria/Lista.html'
    queryset = Libro.objects.filter(disponibilidad="disponible")


def get_context_data(self, **kwargs: Any) -> dict(str, Any):
    context = super().get_context_data(**kwargs)

    context['libro_disponibles'] = Libro.objects.filter(disponibilidad="disponible")
    context['libros_prestados'] = Libro.objects.filter(disponibilidad="prestado")

    return context

class Detalles(DetailView):

    model = Libro
    template_name = 'AppLibreria/detalles.html'


class Crear(CreateView):
    model = Libro
    fields = ['titulo','autor','editorial','rating','fechapubli','genero','ISBN','resumen','disponibilidad','portada']
    template_name = 'AppLibreria/crear.html'
    success_url = reverse_lazy('Listado')