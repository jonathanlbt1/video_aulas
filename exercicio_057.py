# EXERCICIO 57 - Estrutura de repetição 'while'

sexo = ''
l = ['M', 'F']
while sexo not in l:
    print('Vc digitou um sexo inválido!')
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
