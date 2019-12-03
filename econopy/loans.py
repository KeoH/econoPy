"""Prestamos module."""

from econopy.constants import ANUAL


class BaseLoan:

    def __init__(self, capital, periodos, interes, tipo_periodo=ANUAL):
        self.capital = capital
        self.periodos = periodos
        self.tipo_periodo = tipo_periodo
        self._interes = interes
        self.cuotas_interes = []
        self.cuotas_amortizacion = []
        self.capital_vivo = []
        self.total_amortizado = []

    @property
    def interest_rate(self):
        return self._interes * self.tipo_periodo


class FrenchLoan(BaseLoan):

    @property
    def quota(self):
        return self.capital * (
            self.interest_rate*(
                1 + self.interest_rate)**self.periodos) / (-1 + (
                    1 + self.interest_rate)**self.periodos)

    # def calcula_tabla_amortizacion(self):
    #     self.capital_vivo.append(self.principal)
    #     self.cuotas_interes.append(0)
    #     self.cuotas_amortizacion.append(0)
    #     self.total_amortizado.append(0)
    #     for periodo in range(1, self.periodos+1):
    #         interes = self.capital_vivo[periodo-1]*self.interes
    #         amortizado = self.cuota - interes
    #         self.cuotas_interes.append(interes)
    #         self.cuotas_amortizacion.append(amortizado)
    #         self.capital_vivo.append(
    #             self.capital_vivo[periodo-1]-amortizado)
    #         self.total_amortizado.append(
    #             self.total_amortizado[periodo-1]+amortizado)
