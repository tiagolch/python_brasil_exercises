'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

import pytest

# value1 = float(input('Digite um numero: '))
# value2 = float(input('Digite um numero: '))
# value3 = float(input('Digite um numero: '))


def descending(value1, value2, value3):
    if value1 > value2 > value3:
        result = [value1, value2, value3]
    elif value1 > value3 > value2:
        result = [value1, value3, value2]
    elif value2 > value1 > value3:
        result = [value2, value1, value3]
    elif value2 > value3 > value1:
        result = [value2, value3, value1]
    elif value3 > value1 > value2:
        result = [value3, value1, value2]
    else:
        result = [value3, value2, value1]

    print(result)
    return result

# descending(value1, value2, value3)


# tests
@pytest.mark.parametrize('value1, value2, value3, expected', [
    (1, 2, 3, [3, 2, 1]),
    (2, 1, 3, [3, 2, 1]),
    (3, 2, 1, [3, 2, 1]),
    (1, 1, 1, [1, 1, 1])
])
def test_descending(value1, value2, value3, expected):
    assert descending(value1, value2, value3) == expected
