import numpy as np
import scipy.linalg as la

nusp = 123045068
magic_ilong = int(str(nusp).replace("0", ""))
magic_ishort = int(str(magic_ilong)[:2])

# Sistema linear para testes - específica para cada aluno
# ------------------------------------------------------------
# Entrada:
#  n: tamanho da mtriz
#  magic_ilong: seed de geração de números aleatórios
#  cond_pow : potência usada na definição do número de condição (inteiro positivo)
#
# Saída:
#   A: Matrix do sistema linear Ax=b
#   b: lado diretiro do sistema Ax=b
#   a: matriz aumentada [A|b]


def meu_sistema_linear(n=100, magic_ilong=magic_ilong, cond_pow=8):

    # Tamanho do sistema
    #n = 20

    np.random.seed(magic_ilong)

    # Gera matriz aleatória com número de condição alto usando decomposição QR
    cond = np.log(10**cond_pow)  # Numero de condição
    exp_vec = np.arange(-cond/4., cond * (n + 1) /
                        (4 * (n - 1)), cond/(2.*(n-1)))[:n]
    s = np.exp(exp_vec)
    S = np.diag(s)
    U, _ = la.qr((np.random.rand(n, n) - 5.) * 200)
    V, _ = la.qr((np.random.rand(n, n) - 5.) * 200)
    A = U.dot(S).dot(V.T)
    A = A.dot(A.T)  # Simétrica

    # Vetor b - vamos gerar b tal que a solução seja sempre um vetor com 1
    x = np.ones((n))
    b = A@x

    # Matrix aumentada aleatória a=[A|b]
    a = np.c_[A, b]

    np.set_printoptions(precision=3, suppress=True)
    # print("A:" , A[:10, :10]) #imprimir só o começo da matriz
    # print()
    # print("b:", b[:10]) #imprimir só o começo do vetor b
    # print()
    # print("a:", a) #imprimir a matriz aumentada

    return A, b, a
