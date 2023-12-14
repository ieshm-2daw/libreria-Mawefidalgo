from django.urls import path
from . import views
from .views import Listado, Detalles, Crear, Borrar, Editar, PrestamoView, ListTodosLibros, DevolucionView

urlpatterns = [
    path('',Listado.as_view(), name='Listado'),
    path('detalles/<int:pk>/', Detalles.as_view(), name='detalles'),
    path('nuevo', Crear.as_view(),name='crear'),
    path('borrar/<int:pk>/',Borrar.as_view(),name='borrar'),
    path('editar/<int:pk>/', Editar.as_view(), name='editar'),
    path('prestamo/<int:pk>/', PrestamoView.as_view(), name='prestamo'),
    path('todos',ListTodosLibros.as_view(), name='todos'),
    path('devolucion/<int:pk>/', DevolucionView.as_view(), name='devolucion'),
]