import json
import traceback
from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render

from django.shortcuts import render, redirect

from cliente.models import Cliente
from medicamento.models import Medicamento
from venta.models import DetalleVenta, Venta


def lista_ventas(request):
    ventas = Venta.objects.all()
    query = request.GET.get('q')
    print(query)
    if query and query != '':
        ventas = Venta.objects.filter(Q(total__icontains=query) | Q(cliente__cliente_id__icontains=query))
    else:
        ventas = Venta.objects.all()
    data = {}
    print(ventas)
    data['ventas'] = ventas
    """
            Metodo view_crear_proyecto::

                    def view_crear_proyecto(request):

            Metodo para renderizar formulario crear proyecto, verificando los permisos del usuario que obtiene del request

            Args:
                request: Es un objeto de solicitud que recibe con metodo GET
            Returns:
                    Render de formulario crear proyecto, y mensajes
        """
    return render(request, "listar_ventas.html", {"data": data})


def view_crear_venta(request):
    """
            Metodo view_crear_proyecto::

                    def view_crear_proyecto(request):

            Metodo para renderizar formulario crear proyecto, verificando los permisos del usuario que obtiene del request

            Args:
                request: Es un objeto de solicitud que recibe con metodo GET
            Returns:
                    Render de formulario crear proyecto, y mensajes
        """
    return render(request, "crear-ventas.html", {})


def crear_venta_post(request):
    post_data_json = request.POST['data']
    data = json.loads(post_data_json)
    print(request.POST)
    venta = Venta()
    venta.cliente = Cliente.objects.get(cliente_id=data['cliente'])
    fecha_venta = datetime.now()
    venta.fecha_venta = fecha_venta
    detalles = data['detalles_venta']
    venta.total = data['total']
    detalle_venta = []
    for d in detalles:
        print(d)
        detalle = DetalleVenta()
        detalle.medicamento = Medicamento.objects.get(medicamento_id=d['producto'])
        detalle.cantidad = d['cantidad']
        detalle.precio_unitario = d['precioUnitario']
        detalle.sub_total = d['precioTotal']
        detalle_venta.append(detalle)
    try:
        venta.save()
        for d in detalle_venta:
            d.venta = venta
            d.save()
        msg = "La nueva venta -> N° " + str(venta.id) + " con " + str(len(detalle_venta)) + " detalles"
        request.session['msg'] = msg
    except Exception as e:
        msg = "Ocurrió un error al crear la venta: " + str(e)
        request.session['msgerror'] = msg
        print(msg)  # Imprime el error en la consola
        traceback.print_exc()
    return redirect("listar_ventas")


def ver_detalle_venta(request, id):
    detalles = DetalleVenta.objects.all().filter(venta_id=id)
    data = {}
    print(detalles)
    data['detalles'] = detalles
    """
            Metodo view_crear_proyecto::

                    def view_crear_proyecto(request):

            Metodo para renderizar formulario crear proyecto, verificando los permisos del usuario que obtiene del request

            Args:
                request: Es un objeto de solicitud que recibe con metodo GET
            Returns:
                    Render de formulario crear proyecto, y mensajes
        """
    return render(request, "lista_detalle_ventas.html", {"data": data})
