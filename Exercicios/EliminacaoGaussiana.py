import time
import numpy as np
import scipy.linalg as la
from Auxiliares import *
from EliminacaoGaussiana.elim_gauss_LU import elim_gauss_LU
from EliminacaoGaussiana.elim_gauss_classico import elim_gauss
from EliminacaoGaussiana.elim_gauss_vetorizada import elim_gauss_vet
from EliminacaoGaussiana.meu_sistema_linear import meu_sistema_linear


def MeuSistemaLinear():
    imprimeTitulo(
        'Chamada: meu_sistema_linear (padrão) - Eliminação Gaussiana')
    print('Retorna A: Matrix do sistema linear Ax=b')
    print('Retorna b: lado diretiro do sistema Ax=b')
    print('Retorna a: matriz aumentada [A|b]')
    print()
    A, b, a = meu_sistema_linear()
    print('A: Matrix do sistema linear Ax=b')
    print(A)
    print('b: lado diretiro do sistema Ax=b')
    print(b)
    print('a: matriz aumentada [A|b]')
    print(a)
    input("Press Enter to continue...")


def Questao32():
    imprimeQuestao(
        3.2, 'Reflexão) Você consegue explicar como essa matriz é gerada e discutir suas propriedades a partir desse código?')
    # Resposta
    imprimeTitulo('Resposta')
    print(
        'Inicialmente é gerado uma semente a partir do magic_ilong que usa o nUSP [np.random.seed(magic_ilong)]')
    print(
        'Calcula-se o número de condições a partir do parâmetro de entrada cond_pow=8 [cond = np.log(10**cond_pow)]:', np.log(10**8))
    cond_pow = 8
    n = 100
    cond = np.log(10**cond_pow)
    print('Cria-se um vetor com np.arange(valorMinimo, valorMaximo, passo), com n=número elementos da matrix onde:')
    print('valorMinimo:-cond/4. :', -cond/4.)
    print('valorMaximo: cond * (n + 1)/(4 * (n - 1)) :',
          cond * (n + 1)/(4 * (n - 1)))
    print('passo:cond/(2.*(n-1):', cond/(2.*(n-1)))
    exp_vec = np.arange(-cond/4., cond * (n + 1) /
                        (4 * (n - 1)), cond/(2.*(n-1)))[:n]
    print('Cria-se o vetor exp_vec')
    print(exp_vec)
    print(
        'Calcula-se o vetor s que é o exponencial do vetor criado [s = np.exp(exp_vec)]')
    s = np.exp(exp_vec)
    print(s)
    print('Calcula uma maxtix inserindo os elementos do vetor como diagonal da matrix')
    print('Exemplo com array (a1,a2)')
    print('a1 00')
    print('00 a2')
    S = np.diag(s)
    print(S)
    print('Cria-se a matrix U e V com n dados aleatórios a partir da função qr que é a decomposição A = QR. onde Q é o ortogonal unitário e R a triangular superior')
    U, _ = la.qr((np.random.rand(n, n) - 5.) * 200)
    print('Mariz U')
    print(U)
    V, _ = la.qr((np.random.rand(n, n) - 5.) * 200)
    print('Mariz V')
    print(V)
    print('Cria-se a matriz A que é o produto vetorial da matriz S com a transposta da matriz V')
    A = U.dot(S).dot(V.T)
    print('Mariz A - original')
    print(A)
    print('Cria-se a matriz simétrica que é  protudo vetorial da matriz A pela sua transposta ')
    A = A.dot(A.T)  # Simétrica
    print('Mariz A - Simétrica')
    print(A)
    print('Cria-se o vetor b tal que a solução seja sempre um vetor com 1')
    x = np.ones((n))
    b = A@x
    print('Vetor b: lado diretiro do sistema Ax=b')
    print(b)
    print('Matrix aumentada aleatória a=[A|b]')
    a = np.c_[A, b]
    print(a)
    input("Press Enter to continue...")


def TesteUsandoMeuSistema(magic_ilong):

    imprimeTitulo('Teste Usando MeuSistema')

    start_time = time.time()
    A, b, a = meu_sistema_linear(300, magic_ilong)
    x = elim_gauss(a)
    tempo_orig = time.time() - start_time
    print()

    print("Solução", x[:10])  # imprime só alguns elementos da solução
    print("\n\nResíduo max|b-Ax|: ", np.max(np.abs(b-A@x)),
          " Tempo que levou: ", tempo_orig, " segundos")
    input("Press Enter to continue...")
    return tempo_orig, x


def TesteUsandoMeuSistemaVetorizado(magic_ilong, tempo_orig, x):

    imprimeTitulo('Teste Usando MeuSistema Vetorizado')

    start_time = time.time()
    A, b, a = meu_sistema_linear(300, magic_ilong)
    x_vet = elim_gauss_vet(a)
    tempo_vet = time.time() - start_time
    print("Solução:", x_vet[:10])  # imprime só alguns elementos da solução
    print("Resíduo max|b-Ax|: ", np.max(np.abs(b-A@x_vet)),
          " Tempo que levou: ", tempo_vet, " segundos")
    print()
    print("Aceleração em relação ao método sem vetorização:",
          tempo_orig/tempo_vet, " vezes mais rápido")
    print("Diferença máxima na solução:", np.max(np.max(x-x_vet)))
    input("Press Enter to continue...")


def TesteUsandoMeuSistemaLU(magic_ilong, tempo_orig, x):

    imprimeTitulo('Teste Usando MeuSistema LU')

    start_time = time.time()
    A, b, a = meu_sistema_linear(300, magic_ilong)
    x_LU, L, U = elim_gauss_LU(A, b)
    tempo_LU = time.time() - start_time
    print("Solução:", x_LU[:10])  # imprime só alguns elementos da solução
    print("Resíduo max|b-Ax|: ", np.max(np.abs(b-A@x_LU)),
          " Tempo que levou: ", tempo_LU, " segundos")
    print()
    print("Aceleração em relação ao método sem vetorização:",
          tempo_orig/tempo_LU, " vezes mais rápido")
    print("Diferença máxima na solução:", np.max(np.max(x-x_LU)))
    print('\nTeste LU: ')
    print(np.max(np.max(np.abs(L@U-A))))
    input("Press Enter to continue...")


def Questao33():
    imprimeQuestao(
        3.3, 'Esse método que implementamos parece funcionar, mas está muito lento! Como podemos melhorar a sua performance?')
    # Resposta
    imprimeTitulo('Resposta')
    print('É possível melhorar a performance vetorizando o código')
    print('Exemplo:')
    print('     for k in range(n+1):')
    print('         a[j,k] = a[j,k] - ratio * a[i,k]')
    print('Fica desta forma:')
    print('a[j, :] = a[j, :] - ratio * a[i, :]')

    input("Press Enter to continue...")


def Questao34():
    imprimeQuestao(
        3.4, 'O resíduo parece bem grande, por que não está mais perto de 10e-16? (que seria o erro de arredondamento esperado para uma aritmética de ponto flutuante com 64 bits (double float)).')
    # Resposta
    imprimeTitulo('Resposta')
    print('Como x é calculado através de: Ux=y => x = y/U temos um acumulo do erro da divisão neste vetor. Por conta disso, o valor do resíduo é maior do que 10e-16')
    input("Press Enter to continue...")


def Questao35():
    imprimeQuestao(
        3.4, 'Você consegue usar essa ideia do LU para fazer diretamente a solução do sistema linear vetorial, com apenas um loop, sem precisar calcular L e U explicitamente como fizemos?')
    # Resposta
    imprimeTitulo('Resposta')
    input("Press Enter to continue...")
# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def EliminacaoGaussiana(titulo, nusp):
    magic_ilong, magic_ishort = MagicNumbers(nusp)
    LimpaTela()
    imprimeTitulo(titulo)
    # MeuSistemaLinear()
    # Questao32()
    # tempo_orig, x = TesteUsandoMeuSistema(magic_ilong)
    # Questao33()
    # Questao34()
    #TesteUsandoMeuSistemaVetorizado(magic_ilong, tempo_orig, x)
    #TesteUsandoMeuSistemaLU(magic_ilong, tempo_orig, x)

    A, b, a = meu_sistema_linear(300, magic_ilong)
    # x = 1
    # y = 2
    # z = 3
    #  x+y+z=6
    # 2x+y-z=1
    #  x-y+z=2
    A = np.array([[1., 1., 1.], [2., 1., -1.], [1., -1., 1.]])
    b = np.array([6., 1., 2.])
    x_LU, L, U = elim_gauss_LU(A, b)

    # Questao35()

    imprimeTraco(180)
