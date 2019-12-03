"""rate module tests."""

from econopy.rates import (cuatrimestral_simple_interest_rate,
                           interes_anual_simple, montly_simple_interest_rate,
                           semestral_simple_interest_rate,
                           trimestral_simple_interest_rate)


def test_montly_simple_interest_rate():
    assert montly_simple_interest_rate(12) == 1.0


def test_cuatrimestral_simple_interest_rate():
    assert cuatrimestral_simple_interest_rate(3) == 1.0


def test_trimestral_simple_interest_rate():
    assert trimestral_simple_interest_rate(4) == 1.0


def test_semestral_simple_interest_rate():
    assert semestral_simple_interest_rate(2) == 1.0


def test_interes_anual_simple():
    assert interes_anual_simple(1, 1) == 1
