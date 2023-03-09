'''
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
'''


import pytest


def input_height():
    height = float(input('Digite sua altura: '))
    return height


def ideal_weight(height):
    weight = (72.7 * height) - 58
    print('O peso ideal é {0:.2f}'.format(weight))
    return '{0:.2f}'.format(weight)


# height = input_height()
# ideal_weight(height)


@pytest.mark.parametrize('height, expected', [
    (1.80, '72.86'),
])
def test_ideal_weight(height, expected):
    assert ideal_weight(height) == expected
