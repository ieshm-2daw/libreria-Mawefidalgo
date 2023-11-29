from django.urls import path
from . import views
from .views import Listado, Detalles, Crear

urlpatterns = [
    path('',Listado.as_view(), name='Listado'),
    path('detalles/<int:pk>/', Detalles.as_view(), name='detalles'),
    path('nuevo', Crear.as_view(),name='crear'),
]