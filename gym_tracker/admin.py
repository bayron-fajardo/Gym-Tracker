from django.contrib import admin
from .models import Usuario, Rutina, Sesion, EjercicioBase


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    

@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ('id_rutina', 'nombre', 'dia', 'id_usuario', 'objetivo')
    list_filter = ('dia',)
    search_fields = ('nombre', 'objetivo')


@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ('id_sesion', 'id_rutina', 'fecha', 'sensaciones')
    list_filter = ('fecha',)


@admin.register(EjercicioBase)
class EjercicioBaseAdmin(admin.ModelAdmin):
    list_display = ('id_ejercicio', 'nombre', 'grupo_muscular', 'descripcion')
    search_fields = ('nombre', 'grupo_muscular')

