from econopy.constants import VAT


def deflate_vat(amount, vat=VAT):
    return amount / (1 + vat)
