from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    licencia = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} (Lic: {self.licencia})"


class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=15)
    precio_dia = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"


class Alquiler(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='alquileres'
    )
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name='alquileres'
    )
    fecha_inicio = models.DateField()
    dias = models.PositiveIntegerField()
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehiculo.placa} - {self.cliente.nombre}"