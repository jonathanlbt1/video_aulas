# EXERCICIO 20 - SORTEANDO UMA ORDEM NA LISTA

from random import shuffle

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'A ordem de apresentação dos trabalhos será: \n{alunos}')
