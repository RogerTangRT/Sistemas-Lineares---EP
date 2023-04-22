import numpy as np
import scipy.linalg as la

from Auxiliares import MagicNumbers, imprimeTitulo

nusp = 123045068
magic_ilong, magic_ishort = MagicNumbers(nusp)

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

    # exp_vec = np.arange(-cond/4., cond * (n + 1) /
    #                    (4 * (n - 1)), cond/(2.*(n-1)))[:n]

    inicio = -cond/4.
    fim = cond * (n + 1) / (4 * (n - 1))
    passo = cond/(2.*(n-1))

    exp_vec = np.arange(inicio, fim, passo)

    # Corta em n posições
    exp_vec = exp_vec[:n]

    # e^(n) = e(inverso de ln)
    s = np.exp(exp_vec)

    # Calcula uma maxtix inserindo os elementos do vetor como diagonal da matrix
    # Exemplo com array (a1,a2,a3,a4,a5)
    # a1 00 00 00 00
    # 00 a2 00 00 00
    # 00 00 a3 00 00
    # 00 00 00 a4 00
    # 00 00 00 00 a5
    S = np.diag(s)

    # Cria matriz com valor aleatório
    # Calculate the decomposition A = Q R where Q is unitary/orthogonal and R upper triangular.
    # Obtém a matrix Q
    U, _ = la.qr((np.random.rand(n, n) - 5.) * 200)
    V, _ = la.qr((np.random.rand(n, n) - 5.) * 200)
    A = U.dot(S).dot(V.T)
    A = A.dot(A.T)  # Simétrica

    # Vetor b - vamos gerar b tal que a solução seja sempre um vetor com 1
    x = np.ones((n))
    # calcula B de forma que o produto de Axb seja sempre 1
    b = A@x

    # Matrix aumentada aleatória a=[A|b]
    # [1 2 3]    [1 2 3 b1]
    # [1 2 3] => [1 2 3 b2]
    # [1 2 3]    [1 2 3 b3]
    a = np.c_[A, b]

    np.set_printoptions(precision=3, suppress=True)
    # print("A:" , A[:10, :10]) #imprimir só o começo da matriz
    # print()
    # print("b:", b[:10]) #imprimir só o começo do vetor b
    # print()
    # print("a:", a) #imprimir a matriz aumentada

    # Verificar se tem determinante nulo
    # Aproveite e inclua no seu código uma condição para dizer se o sistema tem determinante nulo ou não.
    detA = np.linalg.det(A)
    imprimeTitulo('Determinante de A')
    print(detA)
    if (detA == 0):
        imprimeTitulo('Determinante é nulo')

    return A, b, a
