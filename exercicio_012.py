# EXERCICIO 12 - DESCONTO DO PREÇO DE UM PRODUTO

produto = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${produto - (produto*0.05):.2f}.')
