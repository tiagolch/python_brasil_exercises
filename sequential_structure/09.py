'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

import pytest


def input_fahreinheit():
    temp = float(input('Digite a temperatura em Fahreinheit: '))
    return temp


def fahrenheit_to_celcius(value):
    result = 5 * ((value - 32) / 9)
    result = "{0:.2f}".format(result)
    print(f'A temperatura de {value} °F em celcius é {result} °C')
    return result


# value = input_fahreinheit()
# fahrenheit_to_celcius(value)


#Tests
@pytest.mark.parametrize('value, expected', [
    (100, '37.78'),
    (0, '-17.78'),
])
def test_fahrenheit_to_celcius(value, expected):
    assert fahrenheit_to_celcius(value) == expected
