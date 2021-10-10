# EXERCICIO 31 - CALCULANDO O PREÇO DE UMA PASSAGEM DE ÔNIBUS

km = int(input('Qual a distância de sua viagem em km? '))
price = 0
if km <= 200:
    price = 0.50
else:
    price = 0.45
print(f'O preço de sua viagem é R${km * price}')
