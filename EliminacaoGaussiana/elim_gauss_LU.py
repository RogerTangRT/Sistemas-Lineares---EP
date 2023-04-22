import numpy as np
# Método Clássico de Eliminação Gaussiana via decomposição LU
#
# O método recebe como entrada uma matrix A (n x n) e o vetor b (n x 1),
#
# O método retorna a solução do sistema linear Ax=b,
#            ou um erro quando isso não for possível
# Devolve tambem as matrizes L e U da decomposição A=LU


def elim_gauss_LU(A, b):
    # Número de linhas e colunas
    n, m = A.shape

    # Vetor da solução
    x = np.empty((n))

    # Verifica se usuário forneceu uma matriz no formato certo
    if m != n:
        print("Essa matriz não tem dimensões adequadas:", n, m)
        return x

    # Guardo tanto L quanto U em uma única matriz!!!!
    LU = np.eye(n)  # Matriz identidade

    # @ faz multiplicação de matrizes usando numpy
    for i in range(n):
        if LU[i, i] == 0.0:
            print('Ainda não implementei pivotamento :-( ')
            return x
        # Varre linhas superiores (Upper)
        LU[i, i:] = A[i, i:]-LU[i, :i] @ LU[:i, i:]
        # Varre colunas inferiores (Lower)
        LU[(i+1):, i] = (A[(i+1):, i] - LU[(i+1):, :i] @ LU[:i, i]) / LU[i, i]

    # Substituição
    # LUx=b =>  Ly=b,  Ux=y
    y = np.zeros(n)
    # Ly=b
    y[0] = b[0]
    for i in range(1, n, 1):
        # Vetorizei aqui!
        y[i] = (b[i] - np.dot(LU[i, :i], y[:i]))

    # Ux=y
    x = np.zeros(n)
    x[n-1] = y[n-1]/LU[n-1, n-1]
    for i in range(n-2, -1, -1):
        # Vetorizei aqui!
        x[i] = (y[i] - np.dot(LU[i, i+1:], x[i+1:]))/LU[i, i]

    # Forma matrizes L e U, tais que A=LU
    U = np.triu(LU)  # Pega só triangular superior
    L = np.tril(LU)  # Pega só triangular inferior
    np.fill_diagonal(L, 1.0)  # Preenche com 1 a diagonal inferior
    return x, L, U
