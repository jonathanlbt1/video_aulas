# EXERCICIO 34 - CALCULANDO AUMENTO DE SALÁRIO

salario = float(input('Qual é o seu salário atual? R$ '))
if salario > 1250.0:
    salario = salario * 1.10
else:
    salario = salario * 1.15

print(f'Seu salário foi para R${salario:.2f}')
