from django.urls import path
from . import views

urlpatterns = [
    path('todas/', views.todas_facturas, name='todas_facturas'),
    path('pagadas/', views.facturas_pagadas, name='facturas_pagadas'),
    path('cliente/<int:cliente_id>/', views.facturas_por_cliente, name='facturas_por_cliente'),
    path('cliente/<int:cliente_id>/join/', views.facturas_por_cliente_join, name='facturas_por_cliente'),
]