from django.db import models

class Factura(models.Model):
    cliente_id = models.IntegerField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    pagada = models.BooleanField(default=False)
    