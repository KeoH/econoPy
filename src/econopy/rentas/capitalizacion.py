"""Capitalizaciones financieras .. llevar dinero al futuro."""
import rentas


def capitalizar_cantidad_compuesto(cantidad, tipo_interes, numero_periodos):
    """ 
            Capitaliza una cantidad de dinero un determinado número de períodos
            por el metodo compuesto, los cuales han sido pasados en los parámetros. 

    """

    cantidad_capitalizada = cantidad*(1+tipo_interes)**numero_periodos
    return cantidad_capitalizada


def capitalizar_cantidad_simple(cantidad, tipo_interes, numero_periodos):
    """ 
            Capitaliza una cantidad de dinero un determinado número de períodos
            por el metodo simple, los cuales han sido pasados en los parámetros. 

    """

    cantidad_capitalizada = cantidad*(1+(tipo_interes*numero_periodos))
    return cantidad_capitalizada


def capitalizar_renta_compuesto(cuota, tipo_interes, numero_periodos):
    """
            Capitaliza una renta con los datos de cuota, tipo de interes y número
            de períodos pasados como parámetro. Supone todas las cuotas iguales.
    """
    renta_capitalizada = 0

    for i in range(1, numero_periodos+1):
        renta_capitalizada += capitalizar_cantidad_compuesto(cuota, tipo_interes, i)

    return renta_capitalizada
