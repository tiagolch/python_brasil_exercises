'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à 
tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a 
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

import pytest

# value1 = float(input('Digite a primeira nota: '))
# value2 = float(input('Digite a segunda nota: '))


def grade_point_average(value1, value2):
    average = (value1 + value2) / 2
    data = {
        'value1': value1,
        'value2': value2,
        'average': average
    }
    

    if average >= 9:
        concept = 'A'
        status = 'APROVADO'
    elif 7.5 <= average < 9:
        concept = 'B'
        status = 'APROVADO'
    elif 6 <= average < 7.5:
        concept = 'C'
        status = 'APROVADO'
    elif 4 <= average < 6:
        concept = 'D'
        status = 'REPROVADO'
    else:
        concept = 'E'
        status = 'REPROVADO'
     
    data['concept'] = concept
    data['status'] = status

    print(f'Primeira nota: {value1}')
    print(f'Segunda nota:  {value2}')
    print(f'Media:         {data["average"]}')
    print(f'Conceito:      {data["concept"]}')
    print(f'Status:        {data["status"]}')

    return data


# grade_point_average(value1, value2)


#tests
@pytest.mark.parametrize('value1, value2, expected',[
    (10, 10, {
        'value1': 10,
        'value2': 10,
        'average': 10,
        'concept': 'A',
        'status': 'APROVADO'
    }),
    (5, 5, {
        'value1': 5,
        'value2': 5,
        'average': 5,
        'concept': 'D',
        'status': 'REPROVADO'
    }),
])
def test_grade_point_average(value1, value2, expected):
    data = grade_point_average(value1, value2)

    assert data['value1'] == expected['value1']
    assert data['value1'] == expected['value1']
    assert data['average'] == expected['average']
    assert data['concept'] == expected['concept']
    assert data['status'] == expected['status']

