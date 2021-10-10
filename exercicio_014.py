# EXERCICIO 14 - CONVERTENDO TEMPERATURAS

unidade = int(input('Qual unidade de medida da temperatura, C = 1 ou F = 2? '))
if unidade not in [1,2]:
      print('Número inválido!!!')
else:
      temp = float(input('Qual a temperatura: '))
      if unidade == 1:
            new_temp = temp * 1.8 + 32
            print(f'A temperatura de {temp}C corresponde a {new_temp:.1f}F!')
      elif unidade == 2:
            new_temp1 = temp / 1.8 - 32
            print(f'A temperatura de {temp}F corresponde a {new_temp1:.1f}C!')
