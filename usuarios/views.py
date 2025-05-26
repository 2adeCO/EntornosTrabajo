from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # o la url que desees después de registro
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/register.html', {'form': form})
