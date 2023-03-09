'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

import pytest


def labor_calculation(value_hour, hour_month):
    gross_salary = value_hour * hour_month
    ir = gross_salary * 0.11
    inss = gross_salary * 0.08
    sindicate = gross_salary * 0.05
    salary_liquid = gross_salary - (ir + inss + sindicate)
    print(f'+ Salário Bruto : R${gross_salary}')
    print(f'- IR (11%) : R${ir}')
    print(f'- INSS (8%) : R${inss}')
    print(f'- Sindicato ( 5%) : R${sindicate}')
    print(f'= Salário Liquido : R${salary_liquid}')
    return [gross_salary, ir, inss, sindicate, salary_liquid]


# value_hour = float(input('Qual o valor hora? '))
# hour_month = int(input('Quantas horas trabalhadas no mês? '))

# labor_calculation(value_hour, hour_month)


@pytest.mark.parametrize(
    'value_hour, \
     hour_month, \
     expected_gross_salary, \
     expected_ir, \
     expected_inss, \
     expected_sindicate, \
     expected_salary_liquid', [
        (30, 200, 6000, 660.0, 480.0, 300.0, 4560.0),
    ])
def test_labor_calculation(
    value_hour,
    hour_month,
    expected_gross_salary,
    expected_ir,
    expected_inss,
    expected_sindicate,
    expected_salary_liquid
):
    gross_salary, ir, inss, sindicate, salary_liquid = labor_calculation(
        value_hour, hour_month
    )

    assert gross_salary == expected_gross_salary
    assert ir == expected_ir
    assert inss == expected_inss
    assert sindicate == expected_sindicate
    assert salary_liquid == expected_salary_liquid
