'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa 
não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e 
encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

import pytest
import math

# a = float(input('Valor de A: '))
# b = float(input('Valor de B: '))
# c = float(input('Valor de C: '))


def quadratic_equation(a, b, c):
    if a == 0:
        return 'Não é possivel calcular a equação com o valor de A sendo 0'
    
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        result = 'A equação não possui raizes reais'
    elif discriminant == 0 :
        root = -b / (2 * a)
        result =  f"Uma única raiz real: {root:.2f}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        result = f"Duas raízes reais e distintas: {root1:.2f}, {root2:.2f}" 

    print(result) 
    return result

# quadratic_equation(a, b, c)

# tests
@pytest.mark.parametrize('a, b, c, expected', [
    (0, 2, 3, 'Não é possivel calcular a equação com o valor de A sendo 0'),
    (1, 2, 3, 'A equação não possui raizes reais'),
    (1, -6, 9, 'Uma única raiz real: 3.00'),
    (2, 5, -3, 'Duas raízes reais e distintas: 0.50, -3.00'),

    
])
def test_quadratic_equation(a, b, c, expected):
    assert quadratic_equation(a, b, c) == expected
