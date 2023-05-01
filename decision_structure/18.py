'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

from datetime import datetime
import pytest

#date = input('Insira uma data no formato dd/mm/YYYY: ')

def validate_date(date):
    if datetime.strptime(date, "%d/%m/%Y"):
        result = True
    else:
        result = False
    return result


#validate_date(date)


#tests
@pytest.mark.parametrize('date, expected',[
    ('11/11/2023', True),
])
def test_validate_date(date, expected):
    assert validate_date(date) == expected
