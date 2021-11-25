# Exercicio 114 - Usando biblioteca requests

import urllib
import requests


try:
    url = 'http://pudim.com.br/'
    pudim = requests.get(url).status_code
    if pudim == 200:
        print('Sim, o site Pudim está acessivel no momento.')
    else:
        print('O site Pudim, não está no ar!')
finally:
    print("Job Done")


