from django.shortcuts import render
from django.contrib import messages
from .forms import MenuForm
from menu.models import Menu, Union

# Create your views here.
def lista_menus(request):
    publi= Menu.objects.all()
    return render(request,'menus/listar_publicacion.html',{'publi':publi})

def menu_nuevo(request):

    if request.method == "POST":
        formulario = MenuForm(request.POST)
        if formulario.is_valid():
            menu = Menu.objects.create(nombre=formulario.cleaned_data['nombre'], precio=formulario.cleaned_data['precio'])
            for plato_id in request.POST.getlist('platio'):
                union = Union(plato_id=plato_id, menu_id = menu.id)
                union.save()
            messages.add_message(request, messages.SUCCESS, 'Menu Ingresado Correctamente')
    else:
        formulario = MenuForm()
    return render(request, 'menus/menu_editar.html', {'formulario': formulario})

# Create your views here.
