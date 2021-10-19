# EXERCICIO 77 - Tupla

palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')


for w in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[w]} temos ', end=' ')
    for l in palavras[w]:
        if l.lower() in 'aeiou':
            print(l, end=' ')
