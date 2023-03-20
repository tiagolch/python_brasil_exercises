'''
    Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
    (A área de um círculo é pi vezes o raio elevado ao quadrado (A = π r²))
'''

import pytest


def ask_for_the_radius():
    radius = input('what is the radius of the circle? ')
    return float(radius)

def area_calculation(radius):
    area = 3.14 * (float(radius * radius))
    print(f'A area do circulo é: {area}')
    return area

# call the functions
radius = ask_for_the_radius()
area_calculation(radius)


#Test
@pytest.mark.parametrize('radius, expected', [
    (5, 78.5),
    (10, 314.0),
])
def test_area_calculation(radius, expected):
    assert area_calculation(radius) == expected