# EXERCICIO 8 - CALCULANDO UMA DISTÂNCIA EM DIFERENTES UNIDADES DE MEDIDA

d = float(input('Digite uma distância em metros: '))
print(f'A medida de {d}m corresponde a: \n{d/1000}km \n{d/100}hm \n{d/10}dam '
      f'\n{int(d*10)}dm \n{int(d*100)}cm \n{int(d*1000)}mm')
