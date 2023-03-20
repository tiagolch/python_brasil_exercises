'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.

'''

import pytest

def ask_value_hour_month():
    data = []
    value = int(input('Quanto Ganha por hora? '))
    hour_month = int(input('Quantas horas Trabalhadas no mês? '))
    data = [value, hour_month]
    return data


def salary_hour_month(*data):
    value, hour_month = data
    return value * hour_month


# data = ask_value_hour_month()
# print(salary_hour_month(*data))



@pytest.mark.parametrize('value, hour_month, expected', [
    (10, 8, 80),
])
def test_salary_hour_month(value, hour_month, expected):
    assert salary_hour_month(value, hour_month) == expected



