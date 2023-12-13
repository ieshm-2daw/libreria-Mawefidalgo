from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.
class Usuario(AbstractUser):
    dni = models.CharField(max_length=10)
    direccion = models.TextField()
    telefono = models.IntegerField(null=True)

    def __str__(self):
        return self.dni
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    sitioWeb = models.URLField()

    def __str__(self):
        return self.nombre
    

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    biografia = models.TextField
    foto = models.ImageField(upload_to='autores/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.ManyToManyField(Autor)
    editorial= models.ForeignKey(Editorial, on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MaxValueValidator(5)], null=True)
    fechapubli= models.DateField()
    genero= models.CharField(max_length=50)
    ISBN=models.CharField(max_length=13)
    resumen=models.TextField()

    DISPONIBILIDAD_CHOICES=( 
        ('disponible','Disponible'),
        ('prestado','Prestado'),
        ('en_proceso', 'En_Proceso'),
    )
    disponibilidad=models.CharField(max_length=20, choices=DISPONIBILIDAD_CHOICES, default='disponible')
    portada = models.ImageField(upload_to='portadas/', null=True)

    def __str__(self):
        return self.titulo
    
    
class Prestamo(models.Model):
    libro= models.ForeignKey(Libro, on_delete=models.CASCADE)
    fechaPrestamo = models.DateField()
    fechaDevolucion = models.DateField(null=True)
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)

    ESTADO_CHOICES=(
          ('prestado','Prestado'),
          ('devuelto','Devuelto'),
      )

    estadoPrestamo=models.CharField(max_length=20, choices=ESTADO_CHOICES, default='prestado')

    def __str__(self):
        return f"Prestamo de {self.libro.titulo} a {self.usuario}"