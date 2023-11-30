from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    model = Prestamo
    fields = ['libro', 'fechaprestamo', 'fechadevolucion', 'usuario', 'estadoprestamo']