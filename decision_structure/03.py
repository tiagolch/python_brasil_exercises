'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

import pytest


# letter = input('Digite F ou M: ')

def female_or_male(letter):
    if letter.upper() == 'F':
        result = 'Feminino'
    elif letter.upper() == 'M':
        result = 'Masculino'
    else: 
        result = 'Sexo inválido'
    print(f'{result}')
    return result


# female_or_male(letter)


#tests
@pytest.mark.parametrize('letter, expected',[
    ('f', 'Feminino'),
    ('m', 'Masculino'),
    ('h', 'Sexo inválido'),
])
def test_female_or_male(letter, expected):
    assert female_or_male(letter) == expected
