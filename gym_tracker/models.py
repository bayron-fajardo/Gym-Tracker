from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    
    id_usuario = models.CharField(max_length=20, primary_key=True, editable=False)
    email = models.EmailField()
    
    
    def save(self, *args, **kwargs):
        if not self.id_usuario:
            ultimo = Usuario.objects.all().order_by('id_usuario').last()
            ultimo_num = int(ultimo.id_usuario[4:]) + 1 if ultimo else 1
            self.id_usuario = f"2025{ultimo_num:04d}"
        super().save(*args, **kwargs)
    