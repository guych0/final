from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_menus, name ='lista_menus'),
    url(r'^menu/nuevo/$', views.menu_nuevo, name='menu_nuevo'),
    ]
