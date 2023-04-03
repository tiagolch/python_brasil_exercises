'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde 
a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao 
Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

import pytest


# value_hour = float(input('Valor hora: '))
# hour_worked = int(input('Horas Trabalhadas: '))

def payment(value_hour, hour_worked):
    gross_salary = value_hour * hour_worked
    data = {'gross_salary': gross_salary}

    if gross_salary <= 900:
        ir_percent = 0
    elif 900 < gross_salary <= 1500:
        ir_percent = 0.05
    elif 1500 < gross_salary <= 2500:
        ir_percent = 0.10
    else:
        ir_percent = 0.20

    data['ir'] = data["gross_salary"] * ir_percent
    data['inss'] = data["gross_salary"] * 0.10
    data['fgts'] = data["gross_salary"] * 0.11
    data['total_discount'] = data['ir'] + data['inss']
    data['net_salary'] = gross_salary - data['total_discount']

    print(
        f'Salário Bruto: ({value_hour} * {hour_worked})....: R${data["gross_salary"]}')
    print(f'(-) IR ({ir_percent}%)..................: R${data["ir"]}')
    print(f'(-) INSS ( 10%)................: R${data["inss"]}')
    print(f'FGTS (11%).....................: R${data["fgts"]}')
    print(f'Total de descontos.............: R${data["total_discount"]}')
    print(f'Salário Liquido................: R${data["net_salary"]}')

    return data


# payment(value_hour, hour_worked)

# tests
@pytest.mark.parametrize('value_hour, hour_worked, expected', [
    (30, 220, {'gross_salary': 6600.00,
               'ir': 1320.00,
               'inss': 660.00,
               'fgts': 726.00,
               'total_discount': 1980.00,
               'net_salary': 4620.00}),
    (5, 220, {'gross_salary': 1100.00,
              'ir': 55.00,
              'inss': 110.00,
              'fgts': 121.00,
              'total_discount': 165.00,
              'net_salary': 935.00}),
])
def test_payment(value_hour, hour_worked, expected):
    data = payment(value_hour, hour_worked)

    assert data['gross_salary'] == expected['gross_salary']
    assert data['ir'] == expected['ir']
    assert data['inss'] == expected['inss']
    assert data['fgts'] == expected['fgts']
    assert data['total_discount'] == expected['total_discount']
    assert data['net_salary'] == expected['net_salary']
