# DESAFIO 004

n = input()
print(f'{n} é do tipo primitivo', type(n))
print(f'{n} é alpha numérico?', n.isalnum())
print(f'{n} está escrito em letras minúsculas?', n.islower())
print(f'{n} é numerico?', n.isnumeric())
print(f'{n} é um título?', n.istitle())
print(f'{n} só tem espaços?', n.isspace())
