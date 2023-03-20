'''
    Faça um Programa que calcule a área de um quadrado, 
    em seguida mostre o dobro desta área para o usuário.
'''
import pytest


def calculate_square_area(value):
    return float(value * value)


@pytest.mark.parametrize('value, expected', [
    (1, 1),
    (2, 4),
    (10, 100)
])
def test_calculate_square_area(value, expected):
    assert calculate_square_area(value) == expected
