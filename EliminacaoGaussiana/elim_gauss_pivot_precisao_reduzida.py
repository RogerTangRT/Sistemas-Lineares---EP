import numpy as np
# Método Clássico de Eliminação Gaussiana com aritmética de ponto flutuante restrita
#    e condensação pivotal parcial
#
# O método recebe como entrada uma matrix aumentada a=[A,b] referente ao
#    sistema linear Ax=b, com A (n x n) e o vetor b (n x 1),
# O método recebe também o número de algarismos significativos a serem usados nas contas
#
# O método retorna a solução do sistema linear Ax=b,
#            ou um erro quando isso não for possível


def elim_gauss_pivot_parcial_precisao_reduzida(a_orig, sigfig=3):

    # IMPLEMENTAR PIVOTAMENTO PARCIAL

    # Faço uma cópia, para não estragar a matriz original
    a = np.copy(a_orig)

    # Número de linhas e colunas
    n, m = a.shape

    # Vetor da solução
    x = np.empty((n))

    # Verifica se usuário forneceu uma matriz no formato certo
    if m != n+1:
        print("Essa matriz não tem dimensões adequadas:", n, m)
        return x

    # Escalonamento
    for i in range(n):
        if a[i, i] == 0.0:
            print('Ainda não implementei pivotamento :-( ')
            return x

        for j in range(i+1, n):
            ratio = round(a[j, i]/a[i, i], sigfig)
            # Vetorizei aqui!
            for k in range(n+1):
                a[j, k] = round(
                    a[j, k] - round(ratio * a[i, k], sigfig), sigfig)

    # Substituição
    x[n-1] = round(a[n-1, n]/a[n-1, n-1], sigfig)

    for i in range(n-2, -1, -1):
        # Vetorizei aqui!
        x[i] = a[i, n]
        for j in range(i+1, n):
            x[i] = round(x[i] - round(a[i, j]*x[j], sigfig), sigfig)
        x[i] = round(x[i]/a[i, i], sigfig)

    return x
