'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

import pytest

# value = int(input('Digite um numero: '))


def positive_or_negative(value):
    if value > 0:
        result = 'positivo'
    elif value < 0:
        result = 'negativo'
    else:
        result = 'neutro'
    print(f'{value} é um numero {result}')
    return result

# positive_or_negative(value)

# tests
@pytest.mark.parametrize('value, expected', [
    (2, 'positivo'),
    (-2, 'negativo'),
    (0, 'neutro'),
])
def test_positive_or_negative(value, expected):
    assert positive_or_negative(value) == expected
