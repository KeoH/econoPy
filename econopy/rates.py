"""Rates module."""

from econopy.constants import CUATRIMESTRAL, MENSUAL, SEMESTRAL, TRIMESTRAL


def simple_interest_rate(rate, temp_mode=MENSUAL):
    return rate / temp_mode


def montly_simple_interest_rate(rate):
    return simple_interest_rate(rate, MENSUAL)


def semestral_simple_interest_rate(rate):
    return simple_interest_rate(rate, SEMESTRAL)


def cuatrimestral_simple_interest_rate(rate):
    return simple_interest_rate(rate, CUATRIMESTRAL)


def trimestral_simple_interest_rate(rate):
    return simple_interest_rate(rate, TRIMESTRAL)


def interes_anual_simple(rate, temp_mode):
    return rate * temp_mode
