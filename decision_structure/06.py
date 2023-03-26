'''
Faça um Programa que leia três números e mostre o maior deles.
'''

import pytest

# value1 = float(input('Valor 1: '))
# value2 = float(input('Valor 2: '))
# value3 = float(input('Valor 3: '))


def larger_number(value1, value2, value3):
    if value3 > value2 and value3 > value1:
        result = value3
    elif value1 > value2 and value1 > value3:
        result = value1
    else:
        result = value2
    print(result)
    return result


# larger_number(value1, value2, value3)

# tests
@pytest.mark.parametrize('value1, value2, value3, expected', [
    (1, 2, 3, 3),
    (3, 2, 1, 3),
    (22, 21, 33, 33),
    (0, 0, 1, 1),
    (0, 0, 0, 0),
])
def test_larger_number(value1, value2, value3, expected):
    assert larger_number(value1, value2, value3) == expected
