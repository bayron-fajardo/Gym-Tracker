from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    
    id_usuario = models.CharField(max_length=20, primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    
    
    def save(self, *args, **kwargs):
        if not self.id_usuario:
            ultimo = Usuario.objects.all().order_by('id_usuario').last()
            ultimo_num = int(ultimo.id_usuario[4:]) + 1 if ultimo else 1
            self.id_usuario = f"2025{ultimo_num:04d}"
        super().save(*args, **kwargs)

class Rutina(models.Model):
    
    opciones_dias = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    
    id_rutina = models.CharField(max_length=20, primary_key=True, editable=False)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='rutinas')
    nombre = models.CharField(max_length=250)
    dia = models.CharField(max_length=10,
                           choices=opciones_dias,
                           default=opciones_dias[0])
    descripcion = models.CharField(max_length=250)
    objetivo = models.CharField(max_length=250)
    
    def __str__(self):
        return f'{self.nombre} ({self.dia})'
    

class Sesion(models.Model):
    id_sesion = models.CharField(max_length=20, primary_key=True, editable=False)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    fecha = models.DateField()
    sensaciones = models.CharField(max_length=250)

class EjercicioBase(models.Model):
    id_ejercicio = models.CharField(max_length=20, primary_key=True, editable=False)
    nombre = models.CharField(max_length=250)
    grupo_muscular = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)