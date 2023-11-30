from django.urls import path
from . import views
from .views import Listado, Detalles, Crear, Borrar, Editar

urlpatterns = [
    path('',Listado.as_view(), name='Listado'),
    path('detalles/<int:pk>/', Detalles.as_view(), name='detalles'),
    path('nuevo', Crear.as_view(),name='crear'),
    path('borrar/<int:pk>/',Borrar.as_view(),name='borrar'),
    path('editar/<int:pk>/', Editar.as_view(), name='editar'),
]