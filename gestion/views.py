from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Vehiculo, Alquiler
from .forms import ClienteForm, VehiculoForm, AlquilerForm


# --- VISTA DE INICIO ---
def inicio(request):
    contexto = {
        'total_clientes': Cliente.objects.count(),
        'total_vehiculos': Vehiculo.objects.count(),
        'total_alquileres': Alquiler.objects.count(),
    }
    return render(request, 'gestion/inicio.html', contexto)


# --- CRUD CLIENTE ---
def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/cliente_lista.html', {'clientes': clientes})


def cliente_crear(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_lista')
    return render(request, 'gestion/formulario.html', {
        'form': form,
        'titulo': 'Registrar Cliente',
        'url_cancelar': 'cliente_lista',
    })


def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_lista')
    return render(request, 'gestion/formulario.html', {
        'form': form,
        'titulo': f'Editar Cliente: {cliente.nombre}',
        'url_cancelar': 'cliente_lista',
    })


def cliente_eliminar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_lista')
    return render(request, 'gestion/confirmar_eliminar.html', {
        'objeto': cliente,
        'tipo': 'el cliente',
        'url_cancelar': 'cliente_lista',
    })


# --- CRUD VEHÍCULO ---
def vehiculo_lista(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'gestion/vehiculo_lista.html', {'vehiculos': vehiculos})


def vehiculo_crear(request):
    form = VehiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehiculo_lista')
    return render(request, 'gestion/formulario.html', {
        'form': form,
        'titulo': 'Registrar Vehículo',
        'url_cancelar': 'vehiculo_lista',
    })


def vehiculo_editar(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    form = VehiculoForm(request.POST or None, instance=vehiculo)
    if form.is_valid():
        form.save()
        return redirect('vehiculo_lista')
    return render(request, 'gestion/formulario.html', {
        'form': form,
        'titulo': f'Editar Vehículo: {vehiculo.placa}',
        'url_cancelar': 'vehiculo_lista',
    })


def vehiculo_eliminar(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculo_lista')
    return render(request, 'gestion/confirmar_eliminar.html', {
        'objeto': vehiculo,
        'tipo': 'el vehículo',
        'url_cancelar': 'vehiculo_lista',
    })


# --- CRUD ALQUILER ---
def alquiler_lista(request):
    alquileres = Alquiler.objects.select_related('cliente', 'vehiculo').all()
    return render(request, 'gestion/alquiler_lista.html', {'alquileres': alquileres})


def alquiler_crear(request):
    form = AlquilerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('alquiler_lista')
    return render(request, 'gestion/formulario.html', {
        'form': form,
        'titulo': 'Registrar Alquiler',
        'url_cancelar': 'alquiler_lista',
    })


def alquiler_editar(request, pk):
    alquiler = get_object_or_404(Alquiler, pk=pk)
    form = AlquilerForm(request.POST or None, instance=alquiler)
    if form.is_valid():
        form.save()
        return redirect('alquiler_lista')
    return render(request, 'gestion/formulario.html', {
        'form': form,
        'titulo': f'Editar Alquiler #{alquiler.pk}',
        'url_cancelar': 'alquiler_lista',
    })


def alquiler_eliminar(request, pk):
    alquiler = get_object_or_404(Alquiler, pk=pk)
    if request.method == 'POST':
        alquiler.delete()
        return redirect('alquiler_lista')
    return render(request, 'gestion/confirmar_eliminar.html', {
        'objeto': alquiler,
        'tipo': 'el alquiler',
        'url_cancelar': 'alquiler_lista',
    })