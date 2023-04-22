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

    A, b, a = meu_sistema_linear(30)

    for sigfig in range(4, 16):
        imprimeTitulo(
            'Chamada: elim_gauss vetorizada reduzida (ROUND)(a) - Eliminação Gaussiana')
        imprimeTitulo('Retorna Solução sistema linear Ax=b')
        start_time = time.time()
        x_vet = elim_gauss_precisao_reduzida(a, sigfig)
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
    imprimeTitulo(titulo)

    # ----------------------------------------------------------------------------
    # Imprime mágic Number
    # ----------------------------------------------------------------------------
    print("nusp  =", nusp)
    magic_ilong = int(str(nusp).replace("0", ""))
    magic_ishort = int(str(magic_ilong)[:2])
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)
    Questao41(nusp)

    imprimeTraco(180)
