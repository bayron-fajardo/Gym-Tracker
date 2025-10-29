from django.urls import path
from .views import *

urlpatterns = [
   path('', iniciar_sesion, name='login'),
   path('registrarse/', registrarse, name='registrarse'),
   path('home/', home, name='home'),
]
