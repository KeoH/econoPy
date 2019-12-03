"""utils module tests."""

from econopy.utils import deflate_vat


def test_vat():
    defl = deflate_vat(100)
    assert defl == 100 / 1.21
