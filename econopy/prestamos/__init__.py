import rentas


class PrestamoFrances:

    cuota = 0
    principal = 10
    interes_anual = 0.1
    interes = 0.01
    periodos = 1
    tipo_periodo = rentas.ANUAL
    cuotas_interes = []
    cuotas_amortizacion = []
    capital_vivo = []
    total_amortizado = []

    def __init__(self):
        pass

    def calcula_interes(self):
        self.interes = self.interes_anual / self.tipo_periodo

    def calcula_cuota(self):
        self.calcula_interes()
        cuota = self.principal * \
            ((self.interes*(1+self.interes)**self.periodos) /
             (-1+(1+self.interes)**self.periodos))
        self.cuota = cuota

    def calcula_tabla_amortizacion(self):
        self.capital_vivo.append(self.principal)
        self.cuotas_interes.append(0)
        self.cuotas_amortizacion.append(0)
        self.total_amortizado.append(0)
        for periodo in range(1, self.periodos+1):
            interes = self.capital_vivo[periodo-1]*self.interes
            amortizado = self.cuota - interes
            self.cuotas_interes.append(interes)
            self.cuotas_amortizacion.append(amortizado)
            self.capital_vivo.append(self.capital_vivo[periodo-1]-amortizado)
            self.total_amortizado.append(
                self.total_amortizado[periodo-1]+amortizado)

    def pinta_cuadro(self):
        self.calcula_cuota()
        self.calcula_tabla_amortizacion()
        print(" "+"-"*69)
        print("| Periodo | Cuota | Capital Vivo | Cuota Interes | Cuota Amortizacion |")
        print(" "+"-"*69)
        for i in range(1, self.periodos+1):
            print("| {} | {} | {} | {} | {} |").format(i, round(self.cuota, 2), round(
                self.capital_vivo[i], 2), round(self.cuotas_interes[i], 2), round(self.cuotas_amortizacion[i], 2))
