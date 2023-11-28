from django.urls import path
from . import views
from .views import Listado, Detalles

urlpatterns = [
    path('',Listado.as_view(), name='Listado'),
    path('detalles', Detalles.as_view(), name='detalles')
]