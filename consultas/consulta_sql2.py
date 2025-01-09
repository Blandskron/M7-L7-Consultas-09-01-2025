import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consultas.settings')  # Cambia "myproject" por el nombre de tu carpeta de configuración
django.setup()

from consulta_sql.models import Factura
from consulta_orm.models import Cliente
import random

# Poblar la tabla Factura (consulta_sql)
def poblar_facturas():
    clientes = Cliente.objects.all()
    for _ in range(20):  # Generar 20 facturas
        cliente = random.choice(clientes)
        Factura.objects.create(
            cliente_id=cliente.id,
            importe=random.uniform(100, 5000),  # Importe aleatorio entre 100 y 5000
            pagada=random.choice([True, False])  # Aleatorio entre pagada o no
        )
    print("Facturas creadas con éxito.")

# Ejecutar la función para poblar las tablas
def main():
    poblar_facturas()
    print("Base de datos poblada con éxito.")

if __name__ == "__main__":
    main()