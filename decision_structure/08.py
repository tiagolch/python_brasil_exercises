'''
Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais 
barato.
'''

import pytest

# value1 = float(input('Valor do primeiro produto: '))
# value2 = float(input('Valor do segundo produto: '))
# value3 = float(input('Valor do terceiro produto: '))


def cheaper(value1, value2, value3):
    if value1 < value2 and value1 < value3:
        result = value1
    elif value2 < value1 and value2 < value3:
        result = value2
    else:
        result = value3
    print(f'{result} é mais barato.')
    return result

# cheaper(value1, value2, value3)

# tests
@pytest.mark.parametrize('value1, value2, value3, expected', [
    (10.0, 11.0, 12.0, 10.0),
    (12.0, 11.0, 10.0, 10.0),
    (11.0, 10.0, 12.0, 10.0),
])
def test_cheaper(value1, value2, value3, expected):
    assert cheaper(value1, value2, value3) == expected
