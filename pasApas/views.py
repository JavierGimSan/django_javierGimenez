from django.shortcuts import redirect, render

def guardar_sesion(request):
    request.session['usuario'] = 'Juan'
    return render(request, 'missatge.html')

def recuperar_sesion(request):
    usuario = request.session.get('usuario', 'Invitado')
    return render(request, 'recuperar_sesion.html', {'usuario': usuario})

def eliminar_sesion(request):
    if 'usuario' in request.session:
        del request.sesion['usuario']
        return redirect('recuperar_sesion')

