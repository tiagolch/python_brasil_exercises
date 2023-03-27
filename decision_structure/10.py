'''
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

import pytest

# print('Em que turno voce estuda?')
# turn = input('Digite "M" para matutino, "V" para vespertino ou "N" para noturno: ')

def study_turn(turn):
    if turn.lower() == 'm':
        result = 'Bom Dia!'
    elif turn.lower() == 'v':
        result = 'Boa Tarde!'
    elif turn.lower() == 'n':
        result = 'Boa Noite!'
    else:
        result = 'Valor Inválido'

    print(result)
    return result

# study_turn(turn)

#tests
@pytest.mark.parametrize('turn, expected',[
    ('m', 'Bom Dia!'),
    ('v', 'Boa Tarde!'),
    ('n', 'Boa Noite!'),
    ('matutino', 'Valor Inválido'),
])
def test_study_turn(turn, expected):
    assert study_turn(turn) == expected
