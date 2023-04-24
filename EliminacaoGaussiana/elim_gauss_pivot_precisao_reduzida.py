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
        # Para evitar multiplicadores maior ou igual a 1 deve-se:
        # Permutar as linhas de forma a manter a coluna ordenada de forma decrescente
        # No caso de indices iguais na coluna, deve-se usar a proxima coluna como ordenação.
        # Exemplo:
        # A = [ [1., 1., 1.],
        #       [2., -1., 1.],
        #       [1., 2., -1.]]
        # deve ficar assim:
        # A = [ [2., -1., 1.],
        #       [1., 2., -1.],
        #       [1., 1., 1.]]
        # TROCA DE LINHA NO PIVOTAMENTO
        if a[i, i]:
            if i > 0:
                linhasAnteriores = a[0:i, 0:]
                corte = a[i:n]
                linhasOrdenadasDescendente = corte[corte[:, i].argsort()[
                    ::-1][:n]]
                # Concatena Linhas anteriores com linhas ordenadas
                a = np.vstack([linhasAnteriores, linhasOrdenadasDescendente])
            else:
                linhasOrdenadasDescendente = a[a[:, i].argsort()[::-1][:n]]
                a = linhasOrdenadasDescendente

        for j in range(i+1, n):
            ratio = round(a[j, i]/a[i, i], sigfig)
            # Vetorizei aqui!
            for k in range(n+1):
                a[j, k] = round(
                    round(a[j, k], sigfig) - round(ratio * a[i, k], sigfig), sigfig)

    # Substituição
    x[n-1] = round(a[n-1, n]/a[n-1, n-1], sigfig)

    for i in range(n-2, -1, -1):
        # Vetorizei aqui!
        x[i] = a[i, n]
        for j in range(i+1, n):
            x[i] = round(x[i] - round(a[i, j]*x[j], sigfig), sigfig)
        x[i] = round(x[i]/a[i, i], sigfig)

    return x
