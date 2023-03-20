'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos).
'''

import pytest


# file_size = int(input('Qual o tamanho do arquivo em MB? '))
# internet_speed = int(input('Qual a velocidade do link em Mbps? '))


def time_download(file_size, internet_speed):
    file_size_bits = file_size * 8 * 1024 * 1024
    link_speed_bps = internet_speed * 1024 * 1024

    download_time_secs = file_size_bits / link_speed_bps

    download_time_mins = download_time_secs / 60

    print(f'{file_size} sera baixado aproximadamente em {round(download_time_mins, 2)} minutos')

    return round(download_time_mins, 2)


# time_download(file_size, internet_speed)


@pytest.mark.parametrize('file_size, internet_speed, expected', [
    (100, 10, 1.33),
    (1024, 6, 22.76)
])
def test_time_download(file_size, internet_speed, expected):
    assert time_download(file_size, internet_speed) == expected
