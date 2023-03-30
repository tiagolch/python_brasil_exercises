'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para 
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
'''

import pytest

# value = float(input('Valor do salario: '))


def salary_increase(value):
    if value <= 280:
        percent = 0.2
    elif 280 < value < 700:
        percent = 0.15
    elif 700 < value < 1500:
        percent = 0.1
    else:
        percent = 0.05

    value_increase = value * percent
    new_value = value + value_increase

    print('_____________________________________________________')
    print(f'Salario antes do reajuste:.......R${value}')
    print(f'Percentual de aumento aplicado:..{percent}')
    print(f'Valor do aumento:................R${value_increase}')
    print(f'Novo salário, após aumento:......R${new_value}')
    print('_____________________________________________________')

    return new_value


# salary_increase(value)


# tests
@pytest.mark.parametrize('value, expected', [
    (100, 120),
    (280, 336),
    (600, 690),
    (1400, 1540),
    (10000, 10500),
])
def test_salary_increase(value, expected):
    assert salary_increase(value) == expected
