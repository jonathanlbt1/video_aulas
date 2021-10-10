# EXERCICIO 6 - CALCULANDO DOBRO, TRIPLO E RAIZ QUADRADA

from time import sleep
nome = input('Qual é seu nome? ')
print()
sleep(2)
print(f'Welcome to our game! {nome}')
print()
sleep(2)
numero = int(input('Digite um número: '))
sleep(1)
print(f'Ahhh... o {numero} é muito fácil!!! Veja só!')
print()
d = numero * 2
t = numero * 3
rq = numero ** (1/2)
sleep(2)
print(f'O dobro de {numero} vale {d}')
print()
sleep(2)
print(f'O triplo de {numero} vale {t}')
print()
sleep(2)
print(f'A raiz quadrada de {numero} é igual a {rq:.3f}')
