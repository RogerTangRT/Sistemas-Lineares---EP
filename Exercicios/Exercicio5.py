import time
import numpy as np
from Auxiliares import *
from EliminacaoGaussiana.elim_gauss_pivot_precisao_reduzida import elim_gauss_pivot_parcial_precisao_reduzida
from EliminacaoGaussiana.meu_sistema_linear import meu_sistema_linear


def Questao51(nusp):
    imprimeQuestao(
        5.1, 'Implemente uma modificação do seu algoritmo de eliminação de Gauss com precisão reduzida agora considerando um pivotamento parcial, ')
    imprimeQuestao(
        5.1, 'trocando as linhas nas etapas do escalonamento de forma a sempre obter um multiplicador em módulo menor que 1.')

    # Resposta
    imprimeTitulo('Resposta')
    # sigfig=  4 Solução: [-0.003 -0.034  0.101 -0.063 -0.133  0.004  0.015  0.056 -0.055  0.046]
    # sigfig=  5 Solução: [0.185 0.152 0.015 0.103 0.324 0.316 0.414 0.156 0.353 0.305]
    # sigfig=  6 Solução: [0.702 0.653 0.718 0.768 0.646 0.678 0.666 0.706 0.687 0.669]
    # sigfig=  7 Solução: [1.054 1.017 1.029 1.066 1.051 1.081 1.051 1.046 1.073 1.074]
    # sigfig=  8 Solução: [1.    1.002 1.    0.999 1.001 1.    1.002 1.    1.    1.   ]
    # sigfig=  9 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 10 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 11 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 12 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 13 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 13 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 13 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    # sigfig= 13 Solução: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

    A, b, a = meu_sistema_linear(20)

    for sigfig in range(4, 16):
        imprimeTitulo(
            'Chamada: elim_gauss pivot precisão reduzida (ROUND)(a) - Eliminação Gaussiana')
        imprimeTitulo('Retorna Solução sistema linear Ax=b')
        start_time = time.time()
        x_vet = elim_gauss_pivot_parcial_precisao_reduzida(a, sigfig)
        print('sigfig=', sigfig)
        tempo_vet = time.time() - start_time
        print()
        print("Solução:", x_vet[:10])  # imprime só alguns elementos da solução
        print("Resíduo max|b-Ax|: ", np.max(np.abs(b-A@x_vet)),
              " Tempo que levou: ", tempo_vet, " segundos")
        input("Press Enter to continue...")


def Questao52():
    imprimeQuestao(
        5.1, 'Aproveite e inclua no seu código uma condição para dizer se o sistema tem determinante nulo ou não.')
    # Resposta
    imprimeTitulo('Resposta')
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def Exercicio5(titulo, nusp):
    imprimeTitulo(titulo)

    # ----------------------------------------------------------------------------
    # Imprime mágic Number
    # ----------------------------------------------------------------------------
    print("nusp  =", nusp)
    magic_ilong, magic_ishort = MagicNumbers(nusp)
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)
    Questao51(nusp)
    Questao52()

    imprimeTraco(180)
