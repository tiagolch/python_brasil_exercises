'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import pytest


def number_of_cans(square_meters):
    price = 80.00
    liters = square_meters / 3
    if liters <= 18:
        cans = 1
        price = price * cans
        print(f'{cans} Lata a R${price:.2f}')
        data = [f'{cans}', f'{price:.2f}']
    else:
        cans = liters / 18
        if cans > int(cans):
            cans += 1
        cans = int(cans)
        price = price * cans
        print(f'{cans} Latas a R${price:.2f}')
        data = [f'{cans}', f'{price:.2f}']
    return data



# square_meters = int(input('Digite quantos metros quadrados desejado: '))
# number_of_cans(square_meters)


@pytest.mark.parametrize('square_meters, quantity_expected, price_expected', [
    (54, '1', '80.00'),
    (55, '2', '160.00'),
])
def test_number_of_cans(square_meters, quantity_expected, price_expected):
    quantity, price = number_of_cans(square_meters)

    assert quantity == quantity_expected
    assert price == price_expected
