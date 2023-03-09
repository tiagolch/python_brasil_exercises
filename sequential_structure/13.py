'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''

import pytest


def input_height():
    height = float(input('Digite sua altura: '))
    return height


def ideal_weight(height):
    weight_man = (72.7 * height) - 58
    weight_woman = (62.1 * height) - 44.7
    weights = [f'{weight_man:.2f}', f'{weight_woman:.2f}']
    print(
        f'Peso ideal para homem {weight_man:.2f} e mulher {weight_woman:.2f}')
    return weights


# height = input_height()
# ideal_weight(height)


@pytest.mark.parametrize('height, expected1, expected2', [
    (1.80, '72.86', '67.08'),
])
def test_ideal_weight(height, expected1, expected2):
    weight_man, weight_woman = ideal_weight(height)
    assert weight_man == expected1
    assert weight_woman == expected2