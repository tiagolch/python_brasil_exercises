'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

import pytest 


def average_(a, b, c, d):
    return (a + b + c + d) / 4


@pytest.mark.parametrize('a, b, c, d, result',[
    (10, 10, 10, 10, 10),
    (5, 10, 5, 10, 7.5),
    (0, 0, 0, 10, 2.5),
    (5.5, 10, 7, 10, 8.125),
])
def test_average_(a, b, c, d, result):
    assert average_(a, b, c, d) == result
