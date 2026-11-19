from django import forms
from .models import Cliente, Vehiculo, Alquiler


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'licencia', 'telefono']
        labels = {
            'nombre': 'Nombre completo',
            'licencia': 'Número de licencia',
            'telefono': 'Teléfono de contacto',
        }


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'placa', 'precio_dia']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'placa': 'Número de placa',
            'precio_dia': 'Tarifa por día ($)',
        }


class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['cliente', 'vehiculo', 'fecha_inicio', 'dias', 'devuelto']
        labels = {
            'cliente': 'Cliente',
            'vehiculo': 'Vehículo asignado',
            'fecha_inicio': 'Fecha de entrega',
            'dias': 'Cantidad de días',
            'devuelto': '¿Vehículo devuelto?',
        }
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        }