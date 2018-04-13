"""Modulo para calculos variados."""

IS = 0.2   # Impuesto de sociedades a aplicar
IVA = 0.21  # Impuesto de valor añadido

COMISION_STORE = 0.3


def deflactar_IVA(cantidad):
    deflactor = 1 + IVA
    return cantidad / deflactor


def calcular_IS(cantidad):
    return cantidad*IS


def calcular_comision(cantidad):
    return cantidad*COMISION_STORE


def beneficio_por_venta(precio_venta):

    siniva = deflactar_IVA(precio_venta)
    comision = calcular_comision(siniva)
    ingreso = siniva - comision
    isoc = calcular_IS(ingreso)
    return ingreso - isoc
