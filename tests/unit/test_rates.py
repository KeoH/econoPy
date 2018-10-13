"""rate module tests."""


def test_montly_simple_interest_rate():
    from econopy.rates import montly_simple_interest_rate
    assert montly_simple_interest_rate(12) == 1.0


def test_cuatrimestral_simple_interest_rate():
    from econopy.rates import cuatrimestral_simple_interest_rate
    assert cuatrimestral_simple_interest_rate(3) == 1.0


def test_trimestral_simple_interest_rate():
    from econopy.rates import trimestral_simple_interest_rate
    assert trimestral_simple_interest_rate(4) == 1.0


def test_semestral_simple_interest_rate():
    from econopy.rates import semestral_simple_interest_rate
    assert semestral_simple_interest_rate(2) == 1.0


def test_interes_anual_simple():
    from econopy.rates import interes_anual_simple
    assert interes_anual_simple(1, 1) == 1
