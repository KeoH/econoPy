"""Capitalizaciones financieras .. llevar dinero al futuro."""


def capitalizar_cantidad_compuesto(amount, rate, periods):
    """Capitaliza una cantidad de dinero.

    Un determinado número de períodos
    por el metodo compuesto, los cuales han sido pasados en los parámetros.
    """
    return amount*(1+rate)**periods


def capitalizar_cantidad_simple(amount, rate, periods):
    """ Capitaliza una cantidad de dinero.

    Un determinado número de períodos por el metodo simple, los
    cuales han sido pasados en los parámetros.
    """
    return amount*(1+(rate*periods))


def capitalizar_renta_compuesto(installment, rate, periods):
    """Capitaliza una renta.

    Con los datos de cuota, tipo de interes y número de períodos
    pasados como parámetro. Supone todas las cuotas iguales.
    """
    amount = 0
    for i in range(1, periods+1):
        amount += capitalizar_cantidad_compuesto(
            installment, rate, i)
    return amount
