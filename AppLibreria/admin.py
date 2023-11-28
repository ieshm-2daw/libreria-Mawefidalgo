from django.contrib import admin
from .models import Usuario, Libro, Editorial, Prestamo, Autor
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Prestamo)
admin.site.register(Autor)