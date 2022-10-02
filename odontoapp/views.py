#OBJECTS.GET = DEVULEVE UNA SOLA FILA QUE CUMPLA LA CONDICION O CONDICIONES
#OBJECTS.FILTER = DEVUELVE MAS DE UNA FILA QUE CUMPLA LA CONDICION O CONDICIONES
#OBJECTS.ALL = DEVUELVE TODO LO DE LA TABLA


from django.shortcuts import render, redirect
from odontoapp.models import *

# Create your views here.
def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    if (request.method == 'POST'):
        #SE OBTIENEN VARIABLES DEL HTML
        usuarioFormulario = request.POST.get('usuario')
        contraseniaFormulario = request.POST.get('contrasenia')

        if (usuario.objects.filter(nombre_usuario = usuarioFormulario).exists()):
            if (usuario.objects.get(nombre_usuario = usuarioFormulario).contrasenia == contraseniaFormulario):
                request.session["nombre_usuario"] = nombre_usuario
                request.session["nombre_completo"] = usuario.objects.get(nombre_usuario = usuarioFormulario).nombre_completo
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'mensaje_error': "Contraseña ingresada no es válida."})
        else:
            return render(request, 'login.html', {'mensaje_error': "El usuario ingresado no existe."})