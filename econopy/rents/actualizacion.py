"""Actualizaciones financieras.
    Traer una cantidad de dinero del futuro a un tipo de interes dado."""


def actualizar_cantidad(amount, rate, pediods):
    return amount / (1 + rate)**pediods


def actualizar_renta(installment, rate, periods):
    amount = 0
    for i in range(1, periods+1):
        amount += actualizar_cantidad(installment, rate, i)
    return amount


def actualizar_renta_perpetua(installment, rate):
    return installment / rate
