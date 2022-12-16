'''
Faça um Programa que peça dois números e imprima a soma.
'''

import pytest


def sum_(a, b):
    return a + b


@pytest.mark.parametrize('a, b, result',[
    (1, 1, 2),
    (1.1, 1, 2.1),
    (-1, 1, 0),
    (2, 1, 3),
])
def test_sum_(a, b, result):
    assert sum_(a, b) == result



