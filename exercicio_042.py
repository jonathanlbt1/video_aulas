# EXERCICIO 42 - ANALISADOR DE TRIANGULOS COM CONDICIONAIS

print('-=' * 20)
print('ANALISADOR DE TRIANGULOS')
print('-=' * 20)

a = float(input('Digite o valor do primeiro seguimento: '))
b = float(input('Digiete o valor do segundo seguimento: '))
c = float(input('Digite o valor do terceiro seguimento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if a == b == c:
        print('Este triangulo é equilátero')
    elif a != b != c != a:
        print('Este triangulo é escaleno')
    else:
        print('Este triangulo é isócenes')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')