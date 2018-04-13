"""Actualizaciones financieras. Traer una cantidad de dinero del futuro a un tipo de interes dado."""


def actualizar_cantidad(cantidad, tipo_interes, numero_de_periodos):

    cantidad_actualizada = cantidad / (1 + tipo_interes)**numero_de_periodos

    return cantidad_actualizada


def actualizar_renta(cuota, tipo_interes, numero_de_periodos):

    cantidad_actualizada = 0

    for i in range(1, numero_de_periodos+1):
        cantidad_actualizada += actualizar_cantidad(cuota, tipo_interes, i)

    return cantidad_actualizada


def actualizar_renta_perpetua(cuota, tipo_interes):

    cantidad_actualizada = cuota / tipo_interes

    return cantidad_actualizada
