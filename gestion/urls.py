from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Rutas Cliente
    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('clientes/nuevo/', views.cliente_crear, name='cliente_crear'),
    path('clientes/editar/<int:pk>/', views.cliente_editar, name='cliente_editar'),
    path('clientes/eliminar/<int:pk>/', views.cliente_eliminar, name='cliente_eliminar'),

    # Rutas Vehículo
    path('vehiculos/', views.vehiculo_lista, name='vehiculo_lista'),
    path('vehiculos/nuevo/', views.vehiculo_crear, name='vehiculo_crear'),
    path('vehiculos/editar/<int:pk>/', views.vehiculo_editar, name='vehiculo_editar'),
    path('vehiculos/eliminar/<int:pk>/', views.vehiculo_eliminar, name='vehiculo_eliminar'),

    # Rutas Alquiler
    path('alquileres/', views.alquiler_lista, name='alquiler_lista'),
    path('alquileres/nuevo/', views.alquiler_crear, name='alquiler_crear'),
    path('alquileres/editar/<int:pk>/', views.alquiler_editar, name='alquiler_editar'),
    path('alquileres/eliminar/<int:pk>/', views.alquiler_eliminar, name='alquiler_eliminar'),
]