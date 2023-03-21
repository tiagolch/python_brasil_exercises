'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

import pytest


# number_a = int(input('Digite o primeiro numero: '))
# number_b = int(input('Digite o segundo numero: '))


def largest_number(number_a, number_b):
    result = number_a if number_a > number_b else number_b
    print(f'O maior numero é {result}')
    return result

# largest_number(number_a, number_b)

# tests
@pytest.mark.parametrize('number_a, number_b, expected', [
    (1, 2, 2),
    (10, 2, 10),
    (-1, 2, 2),
    (1, -2, 1),
    (0, 0, 0),
])
def test_largest_number(number_a, number_b, expected):
    assert largest_number(number_a, number_b) == expected
