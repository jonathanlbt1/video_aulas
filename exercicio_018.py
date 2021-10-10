# EXERCICIO 18 - VALOR DO SENO, COSSENO E TANGENTE COM BASE EM UM ÂNGULO

from math import radians, cos, sin, tan
an = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print(f'O ângulo de {an} tem o SENO de {sen:.2f}')
print(f'O ângulo de {an} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {an} tem a TANGENTE de {tan:.2f}')
