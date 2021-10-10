# EXERCICIO 22 - TRABALHANDO COM STRINGS

from time import sleep

name = input('Digite seu nome completo: ').strip()
sleep(1.5)
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {name.upper()}')
print(f'Seu nome em minúsculas é {name.lower()}')

full_name = name
name = name.split()
first_name = name[0]

print(f'Seu nome tem ao todo {len(full_name) - full_name.count(" ")} caracteres')
print(f'Seu primeiro nome é {first_name} e ele tem {len(first_name)} letras')
print(full_name)
print(first_name)
