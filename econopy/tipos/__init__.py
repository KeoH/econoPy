import rentas

def interes_mensual_simple(tipo_interes_anual):
	tipo = tipo_interes_anual/ rentas.MENSUAL
	return tipo

def interes_semestral_simple(tipo_interes_anual):
	tipo = tipo_interes_anual / rentas.SEMESTRAL
	return tipo

def interes_cuatrimestral_simple(tipo_interes_anual):
	tipo = tipo_interes_anual / rentas.CUATRIMESTRAL
	return tipo

def interes_trimestral_simple(tipo_interes_anual):
	tipo = tipo_interes_anual / rentas.TRIMESTRAL
	return tipo

def interes_anual_simple(tipo_interes, modo_temporal):
	tipo = tipo_interes * modo_temporal
	return tipo
