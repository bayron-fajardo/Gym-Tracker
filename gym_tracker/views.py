from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario, EjercicioBase


def iniciar_sesion(request):
    
    if request.method == 'POST':
        
        usuario = request.POST.get('usuario')
        contrasenia = request.POST.get('contrasenia')
        
        user = authenticate(request, username=usuario, password=contrasenia)
        
        if user is not None:
            login(request,user)
            messages.success(request, f'Bienvenido {usuario}')
            return redirect('home')
            
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            
            
    return render(request, "login.html")

def registrarse(request):
    
    if request.method == 'POST':
        
        usuario = request.POST.get('usuario')
        correo = request.POST.get('correo')
        confirmar_correo = request.POST.get('confirmar_correo')
        contrasenia = request.POST.get('contrasenia')
        confirmar_contrasenia = request.POST.get('confirmar_contrasenia')
        
        if correo != confirmar_correo:
            messages.error(request, 'Los correos no coinciden.')
        elif contrasenia != confirmar_contrasenia:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif Usuario.objects.filter(username=usuario).exists():
            messages.error(request, 'El usuario ya existe.')
        elif Usuario.objects.filter(email=correo).exists():
            messages.error(request, 'El correo ya está registrado.')
        else:
            
            user = Usuario.objects.create_user(
                username=usuario,
                email=correo,
                password=contrasenia
            )
            user.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('iniciar_sesion')

    return render(request, "register.html")
@login_required
def home(request):
    
    ejercicios = EjercicioBase.objects.all()
    
    return render(request, 'home.html', {'ejercicios' : ejercicios})