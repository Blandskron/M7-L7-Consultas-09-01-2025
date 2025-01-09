import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consultas.settings')  # Cambia "myproject" por el nombre de tu carpeta de configuración
django.setup()

from consulta_orm.models import Cliente
from datetime import date

# Poblar la tabla Cliente (consulta_orm)
def poblar_clientes():
    clientes_data = [
        {"nombre": "Juan", "apellidos": "Pérez", "fecha_nacimiento": date(1985, 5, 20), "activo": True},
        {"nombre": "María", "apellidos": "Gómez", "fecha_nacimiento": date(1990, 8, 15), "activo": False},
        {"nombre": "Carlos", "apellidos": "Rodríguez", "fecha_nacimiento": date(1980, 3, 10), "activo": True},
        {"nombre": "Ana", "apellidos": "López", "fecha_nacimiento": date(1995, 12, 25), "activo": False},
        {"nombre": "Gabriela", "apellidos": "Hernández", "fecha_nacimiento": date(2000, 7, 5), "activo": True},
    ]
    
    for cliente in clientes_data:
        Cliente.objects.create(
            nombre=cliente["nombre"],
            apellidos=cliente["apellidos"],
            fecha_nacimiento=cliente["fecha_nacimiento"],
            activo=cliente["activo"]
        )
    print("Clientes creados con éxito.")

# Ejecutar la función para poblar las tablas
def main():
    print("Poblando la base de datos...")
    poblar_clientes()

if __name__ == "__main__":
    main()