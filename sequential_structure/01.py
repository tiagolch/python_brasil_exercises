'''
Faça um Programa que mostre a mensagem "Alo mundo" na tela.
'''

import pytest

def hello_world():
    return 'Hello world'



def test_hello_world():
    assert hello_world() == 'Hello world'
