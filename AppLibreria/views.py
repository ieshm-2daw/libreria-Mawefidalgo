from django.shortcuts import render
from .models import Libro
from django.views import View
from django.views.generic import ListView, DetailView
# Create your views here.
class Listado(ListView):

    model = Libro
    template_name = 'AppLibreria/Lista.html'


class Detalles(DetailView):

    model = Libro
    template_name = 'AppLibreria/detalles.html'