'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

import pytest


# letter = input('Digite uma letra: ')

def vowel_or_consonant(letter):
    if letter.lower() in 'aeiou':
        result = 'Vogal'
    elif letter.lower() in 'bcdfghjklmnpqrstvwxyz':
        result = 'Consoante'
    else:
        result = 'Não é uma letra'
    print(result)
    return result


# vowel_or_consonant(letter)


# tests
@pytest.mark.parametrize('letter, expected', [
    ('a', 'Vogal'),
    ('b', 'Consoante'),
    ('2', 'Não é uma letra'),
])
def test_vowel_or_consonant(letter, expected):
    assert vowel_or_consonant(letter) == expected
