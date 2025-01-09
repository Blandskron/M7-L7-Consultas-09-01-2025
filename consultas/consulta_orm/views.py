from django.shortcuts import render
from .models import Cliente
from django.utils.dateparse import parse_date

def todos_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'consulta_orm/todos_clientes.html', {'clientes': clientes})

def clientes_activos(request):
    clientes = Cliente.objects.filter(activo=True)
    return render(request, 'consulta_orm/clientes_activos.html', {'clientes': clientes})


def clientes_rango_fechas(request):
    inicio = request.GET.get('inicio', None)
    final = request.GET.get('final', None)

    inicio = parse_date(inicio) if inicio else None
    final = parse_date(final) if final else None

    if inicio and final:
        clientes = Cliente.objects.filter(fecha_nacimiento__range=(inicio, final))
    elif inicio:
        clientes = Cliente.objects.filter(fecha_nacimiento__gte=inicio)
    elif final:
        clientes = Cliente.objects.filter(fecha_nacimiento__lte=final)
    else:
        clientes = Cliente.objects.all()

    return render(request, 'consulta_orm/clientes_rango_fechas.html', {
        'clientes': clientes,
        'inicio': inicio,
        'final': final,
    })
