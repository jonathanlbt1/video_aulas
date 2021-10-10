# EXERCICIO 19 - SORTEANDO UM ITEM NA LISTA

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
escolhas = [a1, a2, a3, a4]
escolhido = random.choice(escolhas)
print(f'O aluno escolhido foi {escolhido}')
