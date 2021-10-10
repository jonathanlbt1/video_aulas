# EXERCICIO 27 - TRABALHANDO COM STRINGS

full_name = input('Digite seu nome completo: ').strip().title()
print(f'Muito prazer em te conhecer {full_name}')
full_name = full_name.split()
print(f'Seu primeiro nome é {full_name[0]}')
print(f'Seu último nome é {full_name[-1]}')
