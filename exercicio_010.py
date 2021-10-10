frase = 'Curso em Video Python'
print(frase[::2])
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.split())

# EXERCICIO 10 - COMPRANDO DÓLARES

din = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${din} você pode comprar US${din/3.27:.2f}')