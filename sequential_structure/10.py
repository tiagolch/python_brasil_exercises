'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
F = C x 1,8 + 32
'''

import pytest


def input_celcius():
    celcius = float(input('Digite a temperatura em Celcius: '))
    return celcius


def fahrenheit_to_celcius(celcius):
    fahrenheit = celcius * 1.8 + 32
    print(f'{celcius} °C equivale a {fahrenheit} °F')
    return '{0:.2f}'.format(fahrenheit)


# celcius = input_celcius()
# fahrenheit_to_celcius(celcius)



@pytest.mark.parametrize('value, expected', [
    (30, '86.00'),
    (0, '32.00'),
])
def test_fahrenheit_to_celcius(value, expected):
    assert fahrenheit_to_celcius(value) == expected


