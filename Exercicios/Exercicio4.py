import time

import numpy as np
from Auxiliares import *
from EliminacaoGaussiana.elim_gauss_precisao_reduzida import elim_gauss_precisao_reduzida
from EliminacaoGaussiana.meu_sistema_linear import meu_sistema_linear


def Questao41(nusp):
    imprimeQuestao(
        4.1, 'Implemente uma versão análoga à apresentada no primeiro código de eliminação de Gauss (a função elim_gauss()), ')
    imprimeQuestao(
        4.1, 'mas que agora arredonde cada operação feita para um certo número de algarismos significations.')
    # Resposta
    imprimeTitulo('Resposta')
    # Implemente uma versão análoga à apresentada no primeiro código de eliminação de Gauss (a função elim_gauss()),
    # mas que agora arredonde cada operação feita para um certo número de algarismos significations.
    # Para tanto, use round(número, sigfigs) após cada conta que realizar no algoritmo. TODAS as contas de +-*/ devem ser sempre arredondadas!
    # Coloque sua implementação no espaço abaixo,

    # ========================================================
    # Chama função Eliminação Gaussiana Vetorizada ARREDONDADA
    # ========================================================
    # Teste o seu código considerando a sua matriz aleatória anterior variando o número de algarismos significativos de 4 até 16.
    # Use como tamanho da matriz pelo menos  n≥20
    # Monte uma tabela, ou gráfico, com o erro máximo da solução obtida em relação a solução obtida com precisão máxima do Python
    # (o "x" obtido com algoritmo original, sem arredondamentos).
    # Qual a razão de caimento do erro quando aumentamos 1 algarismo significativo (aproximadamente)?
    #
    # sigfig=  4 Solução: [ 0.003  0.002 -0.103 -0.217 -0.099 -0.212 -0.01   0.015 -0.097 -0.055]
    # sigfig=  5 Solução: [-0.133 -0.016  0.005 -0.23   0.187 -0.02   0.021 -0.2    0.2    0.173]
    # sigfig=  6 Solução: [ 0.463  0.561  0.559 -0.034  0.65   0.04   0.81   0.175  0.925  0.632]
    # sigfig=  7 Solução: [1.038 1.023 0.979 1.068 1.037 1.073 1.018 1.028 1.005 1.03 ]
    # sigfig=  8 Solução: [1.013 1.012 1.017 1.01  1.009 1.008 1.013 1.014 1.011 1.01 ]
    # sigfig=  9 Solução: [1.    1.    1.    1.    1.    1.    1.    0.999 1.    1.   ]
    # sigfig= 10 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 11 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 12 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 13 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 13 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 13 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 13 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

    A, b, a = meu_sistema_linear(30)

    for sigfig in range(4, 16):
        imprimeTitulo(
            'Chamada: elim_gauss vetorizada reduzida (ROUND)(a) - Eliminação Gaussiana')
        imprimeTitulo('Retorna Solução sistema linear Ax=b')
        start_time = time.time()
        x_vet = elim_gauss_precisao_reduzida(a, sigfig)
        print('sigfig=', sigfig)
        tempo_vet = time.time() - start_time
        print()
        print("Solução:", x_vet[:10])  # imprime só alguns elementos da solução
        print("Resíduo max|b-Ax|: ", np.max(np.abs(b-A@x_vet)),
              " Tempo que levou: ", tempo_vet, " segundos")
        input("Press Enter to continue...")


# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def Exercicio4(titulo, nusp):
    LimpaTela()
    imprimeTitulo(titulo)

    # ----------------------------------------------------------------------------
    # Imprime mágic Number
    # ----------------------------------------------------------------------------
    print("nusp  =", nusp)
    magic_ilong, magic_ishort = MagicNumbers(nusp)
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)
    Questao41(nusp)

    imprimeTraco(180)
    input("Press Enter to continue...")
