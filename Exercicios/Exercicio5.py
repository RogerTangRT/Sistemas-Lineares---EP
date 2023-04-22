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
    A, b, a = meu_sistema_linear(30)

    for sigfig in range(4, 16):
        imprimeTitulo(
            'Chamada: elim_gauss pivot precisão reduzida (ROUND)(a) - Eliminação Gaussiana')
        imprimeTitulo('Retorna Solução sistema linear Ax=b')
        start_time = time.time()
        x_vet = elim_gauss_pivot_parcial_precisao_reduzida(a, sigfig)
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
