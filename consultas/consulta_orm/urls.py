from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos_clientes, name='todos_clientes'),
    path('activos/', views.clientes_activos, name='clientes_activos'),
    path('rango-fechas/', views.clientes_rango_fechas, name='clientes_rango_fechas'),
]