# EXERCICIO 71 - Simulador de Caixa Eletrônico

print('===' * 12)
print('{:^36}'.format('BANCO JONATHAN'))
print('===' * 12)

valor = float(input('Que valor você quer sacar? R$'))
total = valor

cedula = 100
total_cedula = 0

while True:
  if total >= cedula:
      total -= cedula
      total_cedula += 1
  else:
      if total_cedula > 0:
          print(f'Total de {total_cedula} cédulas de {cedula}')
      if cedula == 100:
          cedula = 50
      elif cedula == 50:
          cedula = 20
      elif cedula == 20:
          cedula = 10
      elif cedula == 10:
          cedula = 5
      elif cedula == 5:
          cedula = 2
      elif cedula == 2:
          cedula = 1
      total_cedula = 0
      if total == 0:
          break


print('===' * 12)
print('Volte sempre ao BANCO JONATHAN! Tenha um ótimo dia!')
