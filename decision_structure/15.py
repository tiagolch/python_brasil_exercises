'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os 
valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

import pytest

# a = float(input('valor do lado A: '))
# b = float(input('valor do lado B: '))
# c = float(input('valor do lado C: '))


def triangle(a, b, c):
    if a == b == c:
        result = 'Equilátero'
    elif (a == b) or (b == c) or (c == a):
        result = 'Isósceles'
    else:
        result = 'Escaleno'
    return result


# triangle(a, b, c)


# tests
@pytest.mark.parametrize('a, b, c, expected', [
    (2, 2, 2, 'Equilátero'),
    (2, 2, 3, 'Isósceles'),
    (1, 2, 3, 'Escaleno')
])
def test_triangle(a, b, c, expected):
    assert triangle(a, b, c) == expected
