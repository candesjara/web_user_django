from django.shortcuts import render, redirect

from .models import Usuario
from .forms import UsuarioForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Bienvenido al CRUD de usuarios!")


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'crud_user/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'crud_user/formulario_usuario.html', {'form': form})

def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'crud_user/formulario_usuario.html', {'form': form})

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'crud_user/confirmar_eliminar.html', {'usuario': usuario})
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer