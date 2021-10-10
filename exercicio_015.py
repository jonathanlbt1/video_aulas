# EXERCICIO 15 - CALCULANDO DESPESAS DE ALUGUEL DE CARRO

km = float(input('Qual foi a quantidade de quilômetros rodados? '))
dias = int(input('Quantos dias você ficou com ele? '))
km_p = km * 0.15
dias_p = dias * 60
print(f'O total a pagar é ---> R${km_p + dias_p:.2f}')
print(f'Há um desconto de 12% para pagamentos a vista. \nO total fica R${(km_p + dias_p) - ((km_p + dias_p) * 0.12)}')
