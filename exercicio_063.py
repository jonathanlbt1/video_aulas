# EXERCICIO 63 - Sequência de Fibonacci

print('-' * 20)
print('Sequencia de Fibonacci')
print('-' * 20)

termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
fib = t1 + t2

print('~' * 20)
print(f'{t1} -> {t2} -> ', end='')
while termos - 2 != 0:
    print(f'{fib} -> ', end='')
    t1 = t2
    t2 = fib
    fib = t1 + t2
    termos -= 1

print('FIM')
print('~' * 20)