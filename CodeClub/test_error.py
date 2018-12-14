import pytest


def currency_sign_from_name(name):
    mapping = {
        'euro': '€',
        'dollar': '$',
        'pound': '£'
    }

    if name.lower() in mapping:
        return mapping[name.lower()]
    raise ValueError(f'Name of currency not one of ["euro", "dollar", "pound"]')


@pytest.mark.parametrize('currency', [
    ('kroon'),
    ('sekk'),
    ('rubla'),
])
def test_currency_sign_invalid_values(currency):
    with pytest.raises(ValueError) as exception:
        currency_sign_from_name(currency)
    assert str(exception.value) == f'Name of currency not one of ["euro", "dollar", "pound"]'

