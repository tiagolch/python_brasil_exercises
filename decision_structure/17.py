'''
Faça um Programa que peça um número correspondente a um determinado ano e em 
seguida informe se este ano é ou não bissexto.
'''

import pytest


# year = int(input('Digite um ano para saber se é bisexto: '))

def bisext_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        result = True
    else:
        result = False
    
    print(result)
    return result


# bisext_year(year)


#tests
@pytest.mark.parametrize('year, expected',[
    (2000, True),
    (2016, True),
    (2023, False),
])
def test_bisext_year(year, expected):
    assert bisext_year(year) == expected
