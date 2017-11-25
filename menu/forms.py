from django import forms
from .models import Plato, Menu


class MenuForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Menu
        fields = ('nombre', 'precio', 'platio')
def __init__ (self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["platio"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["platio"].help_text = "Ingrese el platio que desea ingresar en el menu"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["platio"].queryset = Actor.objects.all()
