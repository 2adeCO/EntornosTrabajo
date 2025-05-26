from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from .models import Subscripcion, ObjetoColeccionable

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/register.html', {'form': form})


def panel_usuario(request):
    usuario = request.user
    if not hasattr(usuario, 'usuario'):  # Si estás usando el modelo personalizado
        return redirect('login')

    subscripciones = Subscripcion.objects.filter(usuario=usuario.usuario).values_list('categoria', flat=True)
    objetos = ObjetoColeccionable.objects.filter(categoria__in=subscripciones).order_by('-fecha_creacion')
    return render(request, 'usuarios/panel.html', {'objetos': objetos})
