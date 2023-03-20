'''
    Faça um Programa que converta metros para centímetros.
'''
import pytest


def meters_to_centimeters(value) -> int:
    return int(value) * 100


@pytest.mark.parametrize('value, expected',[
    (1, 100),
    (2, 200),
    (10, 1000),
    ('1', 100),
])
def test_meters_to_centimeters(value, expected):
    assert meters_to_centimeters(value) == expected

