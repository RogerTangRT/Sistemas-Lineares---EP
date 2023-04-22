import numpy as np
from Auxiliares import *
from EliminacaoGaussiana.elim_gauss_pivot_precisao_reduzida import elim_gauss_pivot_parcial_precisao_reduzida

# --------------------------------------------------------------------------------
# Calcula vetor de resposta: yk=x6k−magic_ishort∗x5k
# --------------------------------------------------------------------------------


def GeraArrayRespostas(N, magic_ishort):
    # x0 = 1 => y0 = -123045067
    # x1 = 2 => y1 = -3937442112
    # x2 = 3 => y2 = -29899950795
    # x3 = 4 => y3 = -125998145536
    # x4 = 5 => y4 = -384515821875

    y = [0] * 5
    for k in range(0, N, 1):
        x = k+1
        # print('x', k, '=', k+1)
        y[k] = x**6 - magic_ishort * x**5
        # print('y', k, '=', y[k])
    return y

# --------------------------------------------------------------------------------
# Calcula polinômio
# --------------------------------------------------------------------------------


def Polinomio(magic_ishort, sigfig):
    imprimeQuestao(
        6, 'Queremos encontrar um polinômio de grau  n>0 pn(x)=a0+a1x+a2x2+...+anxn')

    # Resposta
    imprimeTitulo('Resposta')
    # p5(x) = a0 + a1x + a2x^2 + a3x^3 + a4x^4 + a5x^5
    # p5(xk) = yk

    N = 5
    y = GeraArrayRespostas(N, magic_ishort)
    imprimeTitulo('Vetor Resposta')
    print(y)

    x = np.array([1, 2, 3, 4, 5])

    v = np.vander(x, N)
    imprimeTitulo('Matriz de Vandermonde')
    print(v)
    a = np.c_[v, y]
    imprimeTitulo('Matriz extendida')
    print(a)

    x_vet = elim_gauss_pivot_parcial_precisao_reduzida(a, sigfig)
    imprimeTitulo('Vetor Resposta')
    print(x_vet)

    input("Press Enter to continue...")


# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def TarefaFinal(titulo, nusp):
    imprimeTitulo(titulo)

    # ----------------------------------------------------------------------------
    # Imprime mágic Number
    # ----------------------------------------------------------------------------
    print("nusp  =", nusp)
    magic_ilong, magic_ishort = MagicNumbers(nusp)
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)
    Polinomio(nusp, 5)

    imprimeTraco(180)
