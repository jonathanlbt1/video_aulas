#EXERCICIO 105 - Analisando e Gerando Dicionários

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos.
    :param sit: Opcional. Indica se deve ou não apresentar a situação do aluno.
    :return: Dicionário com várias informações sobre a situação do aluno.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = float(f"{sum(n) / len(n):.2f}")
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)

help(notas)