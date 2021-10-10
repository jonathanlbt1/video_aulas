# EXERCICIO 35 - ANALISADOR DE TRIANGULOS

print('-=' * 20)
print('ANALISADOR DE TRIANGULOS')
print('-=' * 20)

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digiete o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
