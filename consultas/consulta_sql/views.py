from django.shortcuts import render
from django.db import connection

def todas_facturas(request):
    query = "SELECT * FROM consulta_sql_factura"
    with connection.cursor() as cursor:
        cursor.execute(query)
        columnas = [col[0] for col in cursor.description]
        facturas = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    return render(request, 'consulta_sql/todas_facturas.html', {'facturas': facturas})

def facturas_pagadas(request):
    query = "SELECT * FROM consulta_sql_factura WHERE pagada = TRUE"
    with connection.cursor() as cursor:
        cursor.execute(query)
        columnas = [col[0] for col in cursor.description]
        facturas = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    return render(request, 'consulta_sql/facturas_pagadas.html', {'facturas': facturas})


def facturas_por_cliente(request, cliente_id):
    query = "SELECT * FROM consulta_sql_factura WHERE cliente_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, [cliente_id])
        columnas = [col[0] for col in cursor.description]
        facturas = [dict(zip(columnas, row)) for row in cursor.fetchall()]

    return render(request, 'consulta_sql/facturas_por_cliente.html', {'facturas': facturas})

def facturas_por_cliente_join(request, cliente_id):
    query = """
        SELECT f.*, c.nombre, c.apellidos 
        FROM consulta_sql_factura f
        JOIN consulta_orm_cliente c ON f.cliente_id = c.id
        WHERE f.cliente_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, [cliente_id])
        columnas = [col[0] for col in cursor.description]
        facturas = [dict(zip(columnas, row)) for row in cursor.fetchall()]

    return render(request, 'consulta_sql/facturas_por_cliente_join.html', {'facturas': facturas})
