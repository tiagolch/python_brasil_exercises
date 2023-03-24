'''
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

import pytest


# value1 = float(input('Digite a primeira nota: '))
# value2 = float(input('Digite a segunda nota: '))


def grade_point_average(value1, value2):
    status = {
        "A": 'Aprovado',
        'AD': 'Aprovado com Distinção',
        'R': 'Reprovado'
    }
    average = (value1 + value2) / 2
    if 7 <= average < 10:
        result = status['A']
    elif average == 10:
        result = status['AD']
    else:
        result = status['R']
    print(result)
    return result


# grade_point_average(value1, value2)


# tests
@pytest.mark.parametrize('value1, value2, expected', [
    (4.2, 5, 'Reprovado'),
    (7, 7, 'Aprovado'),
    (10, 10, 'Aprovado com Distinção'),
])
def test_grade_point_average(value1, value2, expected):
    assert grade_point_average(value1, value2) == expected
