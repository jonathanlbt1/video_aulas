# EXERCICIO 53 - Informando se uma frase é palindromo ou não

frase = input('Digite uma frase: ').strip().upper().split()
frase1 = ''.join(frase)
frase2 = frase1[::-1]

# for l in range(len(frase1) -1, -1, -1):
#     frase2 += frase1[l]

if frase1 == frase2:
    print('Yes, your sentence is a palindromo')
else:
    print('No, you are wrong')
