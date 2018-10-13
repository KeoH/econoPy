"""Tipos module."""

from .. import MENSUAL, SEMESTRAL, CUATRIMESTRAL, TRIMESTRAL


def interes_mensual_simple(rate):
    return rate / MENSUAL


def interes_semestral_simple(rate):
    return rate / SEMESTRAL


def interes_cuatrimestral_simple(rate):
    return rate / CUATRIMESTRAL


def interes_trimestral_simple(rate):
    return rate / TRIMESTRAL


def interes_anual_simple(rate, temp_mode):
    return rate * temp_mode
