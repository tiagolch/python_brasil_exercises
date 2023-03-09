'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que 
João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

import pytest


def weight_penalty(weight):
    value_weight_penalty = 4.00
    weight_limit = 50

    if weight > weight_limit:
        weight_excess = weight - weight_limit
        value_penalty = weight_excess * value_weight_penalty
        print(f'Peso excedente {weight_excess:.2f} e valor da multa é {value_penalty:.2f}')
        return [f'{weight_excess:.2f}', f'{value_penalty:.2f}']
    print(f'Peso dentro do limite {weight:.2f}')
    return [f'Peso esta dentro do limite = {weight:.2f}', '']



# weight = float(input('Digite o Peso: '))
# weight_penalty(weight)



# Tests
@pytest.mark.parametrize('weight, expected1, expected2', [
    (51, '1.00', '4.00'),
    (50, 'Peso esta dentro do limite = 50.00', ''),
])
def test_weight_penalty(weight, expected1, expected2):
    weight_excess, value_penalt = weight_penalty(weight)
    assert weight_excess == expected1
    assert value_penalt == expected2




