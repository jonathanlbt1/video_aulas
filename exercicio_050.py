#Exercicio 50 - Criando lista de números pares

s = 0
l = []
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        l.append(n)
print(s)
print(l)
