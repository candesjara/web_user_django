from django.db import models

# Create your models here.
class Usuario(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
