"""utils module tests."""


def test_vat():
    from econopy.utils import deflate_vat
    defl = deflate_vat(100)
    assert defl == 100 / 1.21
