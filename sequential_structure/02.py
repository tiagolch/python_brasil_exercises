'''
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

'''
import pytest


def number(n):
    return f'The number informed was {n}'


@pytest.mark.parametrize('n,result', [
    (1, 'The number informed was 1'),
    (2, 'The number informed was 2'),
    (-1, 'The number informed was -1'),
    (-1.1, 'The number informed was -1.1'),
])
def test_number(n, result):
    assert number(n) == result
