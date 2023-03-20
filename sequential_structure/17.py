'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. 
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias
'''

import pytest

CAN_SIZE = 18  # Liters
CAN_PRICE = 80  # R$
GALLON_SIZE = 3.6  # Liters
GALLON_PRICE = 25  # R$
COVERAGE_PER_LITER = 6  # Square meters per liter
WASTE_FACTOR = 1.1  # 10% slack

# square_area = float(input('Qual o tamanho em metros quadrados? '))
# liters_needed = square_area / COVERAGE_PER_LITER * 1.1


def only_cans(liters_needed):
    cans, price = 0, 0
    data = {
        'cans': cans,
        'price': price
    }

    data['cans'] = int(liters_needed // CAN_SIZE)
    if liters_needed % CAN_SIZE != 0:
        data['cans'] += 1

    data['price'] = data['cans'] * CAN_PRICE

    print(data)
    return data


def only_gallons(liters_needed):
    gallon, price = 0, 0
    data = {
        'gallon': gallon,
        'price': price
    }

    data['gallon'] = int(liters_needed // GALLON_SIZE)
    if liters_needed % GALLON_SIZE != 0:
        data['gallon'] += 1

    data['price'] = data['gallon'] * GALLON_PRICE

    print(data)
    return data


def cans_and_gallons(liters_needed):
    can, gallon, price = 0, 0, 0
    data = {
        'cans': can,
        'gallon': gallon,
        'price': price
    }

    data['cans'] = int(liters_needed / CAN_SIZE)
    data['gallon']  = int((liters_needed - (data['cans'] * CAN_SIZE)) / GALLON_SIZE)
    if liters_needed - (data['cans'] * CAN_SIZE) % GALLON_SIZE != 0:
        data['gallon'] += 1
    data['price'] = (data['cans'] * CAN_PRICE) + (data['gallon'] * GALLON_PRICE)

    data_cans = only_cans(liters_needed)
    data_gallons = only_gallons(liters_needed)


    if data['price'] > data_gallons['price'] > data_cans['price']:
        data['cans'] = 0
        data['gallon'] = data_gallons['gallon']
        data['price'] = data_gallons['price']
    
    elif data['price'] > data_cans['price'] < data_gallons['price']:
        data['cans'] = data_cans['cans']
        data['gallon'] = 0
        data['price'] = data_cans['price']

    else:
        data = data

    return data


# only_cans(liters_needed)
# only_gallons(liters_needed=0)
# cans_and_gallons(liters_needed=0)


@pytest.mark.parametrize('liters_needed, cans_expected, price_expected', [
    (17, 1, 80.0),
    (19, 2, 160.0),
])
def test_only_cans(liters_needed, cans_expected, price_expected):
    data = only_cans(liters_needed)
    cans = data['cans']
    price = data['price']

    assert cans == cans_expected
    assert price == price_expected


@pytest.mark.parametrize('liters_needed, gallons_expected, price_expected', [
    (1, 1, 25.0),
    (17, 5, 125.0),
    (19, 6, 150.0),
])
def test_only_gallons(liters_needed, gallons_expected, price_expected):
    data = only_gallons(liters_needed)
    gallon = data['gallon']
    price = data['price']

    assert gallon == gallons_expected
    assert price == price_expected


@pytest.mark.parametrize('liters_needed, cans_expected, gallons_expected, price_expected', [
    (1, 0, 1, 25.0),
    (17, 1, 0, 80.0),
    (19, 1, 1, 105.0),
])
def test_cans_and_gallons(liters_needed, cans_expected, gallons_expected, price_expected):
    data = cans_and_gallons(liters_needed)
    cans = data['cans']
    gallon = data['gallon']
    price = data['price']

    assert cans == cans_expected
    assert gallon == gallons_expected
    assert price == price_expected
