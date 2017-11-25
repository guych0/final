from django.db import models
from django.contrib import admin

class Plato(models.Model):

    especialidad =   models.CharField(max_length=30)
    ingrediente =  models.CharField(max_length=30)
    def __str__(self):
        return self.especialidad



class Menu(models.Model):

    nombre    = models.CharField(max_length=60)
    precio = models.CharField(max_length=60)
    platio   = models.ManyToManyField(Plato, through='Union')
    def __str__(self):
        return self.nombre



class Union (models.Model):

    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


class UnionInLine(admin.TabularInline):

    model = Union
    extra = 1


class PlatoAdmin(admin.ModelAdmin):

    inlines = (UnionInLine,)


class MenuAdmin (admin.ModelAdmin):

    inlines = (UnionInLine,)
