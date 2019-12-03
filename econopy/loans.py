"""Loan module."""

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
