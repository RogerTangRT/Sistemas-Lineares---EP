import numpy as np

# Método Clássico de Eliminação Gaussiana
#
# O método recebe como entrada uma matrix aumentada a=[A|b],
# com dimensões n linhas por n+1 colunas, tendo b na última
#
# O método retorna a solução do sistema linear Ax=b,
#            ou um erro quando isso não for possível


def elim_gauss(a_orig):
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
            ratio = a[j, i]/a[i, i]
            for k in range(n+1):
                a[j, k] = a[j, k] - ratio * a[i, k]

    # Substituição
    x[n-1] = a[n-1, n]/a[n-1, n-1]

    for i in range(n-2, -1, -1):
        x[i] = a[i, n]

        for j in range(i+1, n):
            x[i] = x[i] - a[i, j]*x[j]

        x[i] = x[i]/a[i, i]

    return x
