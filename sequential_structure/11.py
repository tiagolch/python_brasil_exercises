'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
'''

import pytest


def input_numbers():
    first_number, second_number, third_number = 0, 0, 0
    first_number = int(input('Digite um numero inteiro: '))
    second_number = int(input('Digite outro numero inteiro: '))
    third_number = float(input('Digite um numero Real: '))
    numbers = [first_number, second_number, third_number]
    return numbers


def first_calculation(*numbers):
    first_number, second_number, _ = numbers

    result = (first_number * 2) * (second_number / 2)
    print(result)
    return result


def second_calculation(*numbers):
    first_number, _, third_number = numbers

    result = (first_number * 3) + third_number
    print(result)
    return result


def third_calculation(*numbers):
    _, __, third_number = numbers

    result = third_number ** 3
    print(result)
    return result



# numbers = input_numbers()
# first_calculation(*numbers)
# second_calculation(*numbers)
# third_calculation(*numbers)



## Tests
@pytest.mark.parametrize('value1, value2, value3, expected', [
    (1, 2, 3, 2),
])
def test_first_calculations(value1, value2, value3, expected):
    numbers = [value1, value2, value3]
    assert first_calculation(*numbers) == expected


@pytest.mark.parametrize('value1, value2, value3, expected', [
    (1, 2, 3, 6),
])
def test_second_calculations(value1, value2, value3, expected):
    numbers = [value1, value2, value3]
    assert second_calculation(*numbers) == expected


@pytest.mark.parametrize('value1, value2, value3, expected', [
    (1, 2, 3, 27),
])
def test_third_calculations(value1, value2, value3, expected):
    numbers = [value1, value2, value3]
    assert third_calculation(*numbers) == expected


