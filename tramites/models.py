from django.db import models

# Create your models here.

class Tramite(models.Model):
    TRAMITES_CHOICES = [
        ('DONACION', 'Donación'),
        ('SUCESION', 'Sucesión'),
        ('ACT_DATO', 'Actualización datos')
    ]
    PREFERENCIA_CHOICES = [
        ('CORREO', 'Correo'),
        ('FISICO', 'Dirección Fisioa')
    ]
    ESTADO_CHOICES = [
        ('REGISTRADO', 'Registrado'),
        ('ASESOR', 'Asignado a un asesor'),
        ('TECNICO', 'Asignado a un soporte técnico'),
        ('SOLUCIONADO', 'Solucionado')
    ]
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=300)
    tramite = models.CharField(max_length=8, choices=TRAMITES_CHOICES)
    comunicacion = models.CharField(max_length=6, choices=PREFERENCIA_CHOICES)
    solicitud = models.CharField(max_length=2000)
    estado = models.CharField(max_length=11, choices=ESTADO_CHOICES)
    fecha_registro = models.DateField(auto_now=True)

    def __str__(self):
        return '{} email {}'.format(self.nombre, self.correo)