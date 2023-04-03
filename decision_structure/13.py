'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

import pytest

# day = int(input('Digite um dia entre 1 - 31: '))

def weekday(day):
    domingo = [1, 8, 15, 22, 29]
    segunda = [2, 9, 16, 23, 30]
    terca =   [3, 10, 17, 24, 31]
    quarta =  [4, 11, 18, 25]
    quinta =  [5, 12, 19, 26]
    sexta =   [6, 13, 20, 27]
    sabado =  [7, 14, 21, 28]

    if day in domingo:
        result = 'Domingo'
    elif day in segunda:
        result = 'Segunda'
    elif day in terca:
        result = 'Terca'
    elif day in quarta:
        result = 'Quarta'
    elif day in quinta:
        result = 'Quinta'
    elif day in sexta:
        result = 'Sexta'
    elif day in sabado:
        result = 'Sabado'
    else:
        result = 'Valor inválido'

    print(result)
    return result


# weekday(day)


#tests
@pytest.mark.parametrize('day, expected',[
    (1, 'Domingo'),
    (9, 'Segunda'),
    (24, 'Terca'),
    (11, 'Quarta'),
    (26, 'Quinta'),
    (6, 'Sexta'),
    (28, 'Sabado'),
    (32, 'Valor inválido'),
])
def test_weekday(day, expected):
    assert weekday(day) == expected
