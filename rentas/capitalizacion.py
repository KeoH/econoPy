#
# Capitalizaciones financieras .. llevar dinero al futuro
import rentas

def capitalizar_cantidad_compuesto(cantidad, tipo_interes, numero_periodos):
	cantidad_capitalizada = cantidad*(1+tipo_interes)**numero_periodos
	return cantidad_capitalizada

def capitalizar_cantidad_simple(cantidad, tipo_interes, numero_periodos):
	cantidad_capitalizada = cantidad*(1+(tipo_interes*numero_periodos))
	return cantidad_capitalizada

def capitalizar_renta_compuesto(cuota, tipo_interes, numero_periodos):
	renta_capitalizada = 0

	for i in range(1, numero_periodos+1):
		renta_capitalizada += capitalizar_cantidad(cuota, tipo_interes, i)

	return renta_capitalizada

def interes_mensual_simple(tipo_interes_anual):
	tipo = tipo_interes_anual/ rentas.MENSUAL
	return tipo

def interes_semestral_simple(tipo_interes_anual):
	tipo = tipo_interes_anual / SEMESTRAL
	return tipo

def interes_cuatrimestral_simple(tipo_interes_anual):
	tipo = tipo_interes_anual / CUATRIMESTRAL
	return tipo

def interes_trimestral_simple(tipo_interes_anual):
	tipo = tipo_interes_anual / TRIMESTRAL
	return tipo

def interes_anual_simple(tipo_interes, modo_temporal):
	tipo = tipo_interes * modo_temporal
	return tipo

