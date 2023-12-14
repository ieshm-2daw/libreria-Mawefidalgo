from datetime import date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Prestamo
from django.urls import reverse_lazy
from django.views import View
from typing import Any
from .forms import PrestamoForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# Create your views here.
class Listado(ListView):

    model = Libro
    template_name = 'AppLibreria/Lista.html'
    queryset = Libro.objects.filter(disponibilidad="disponible")


    def get_context_data(self, **kwargs: Any) -> dict:
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


class Borrar(DeleteView):
     model = Libro
     template_name = "AppLibreria/borrar.html"
     success_url = reverse_lazy('Listado')

class Editar(UpdateView):
     model = Libro
     fields = ['titulo','autor','editorial','rating','fechapubli','genero','ISBN','resumen','disponibilidad','portada']
     template_name = 'AppLibreria/editar.html'
     success_url = reverse_lazy('Listado')

class PrestamoView(View):
     
     def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, 'AppLibreria/prestamo.html', {"libro":libro})

     def post(self, request, pk):
          libro = get_object_or_404(Libro, pk=pk)
          libro.disponibilidad = "prestado"
          libro.save()
          
          fecha_Devolucion = date.today() + timedelta(days=15)
          
          Prestamo.objects.create(
               libro=libro,
               fechaPrestamo=date.today(),
               fechaDevolucion = fecha_Devolucion,
               usuario = request.user,
               estadoPrestamo = 'prestado'
          )
          return redirect('Listado')

class DevolucionView(View):

     def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, 'AppLibreria/devolucion.html', {"libro":libro})

     def post(self, request, pk):
          libro = get_object_or_404(Libro, pk=pk)
          libro.disponibilidad = "disponible"
          libro.save()
          
          fecha_Prestamo = date.today() - timedelta(days=15)
          
          
          Prestamo.objects.create(
               libro=libro,
               fechaPrestamo=fecha_Prestamo,
               fechaDevolucion = date.today(),
               usuario = request.user,
               estadoPrestamo = 'devuelto'
          )
          return redirect('Listado')
     

class ListTodosLibros(ListView):

    model = Libro
    template_name = 'AppLibreria/Todos.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
         
         context = super().get_context_data(**kwargs)

         context['libros_devueltos'] = Prestamo.objects.filter(usuario=self.request.user, estadoPrestamo='devuelto')
         context['libros_prestados'] = Prestamo.objects.filter(usuario=self.request.user, estadoPrestamo='prestado')

         return context
    
