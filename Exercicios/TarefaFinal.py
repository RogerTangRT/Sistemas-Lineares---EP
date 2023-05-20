import numpy as np
from Auxiliares import *
from EliminacaoGaussiana.elim_gauss_pivot_precisao_reduzida import elim_gauss_pivot_parcial_precisao_reduzida

# --------------------------------------------------------------------------------
# Calcula vetor de resposta: yk=x^6k−magic_ishort∗x^5k
# --------------------------------------------------------------------------------


def GeraArrayRespostas(n, magic):
    # k = 0-> 5
    # x0 = 0 => y0 = -11
    # x1 = 1 => y1 = -320
    # x2 = 2 => y2 = -2187
    # x3 = 3 => y3 = -8192
    # x4 = 4 => y4 = -21875
    # x5 = 5 => y5 = -46656

    y = [0] * n
    for k in range(0, n, 1):
        x = k+1
        print('K=', k, 'x =', x)
        y[k] = x**6 - magic * x**5
        print('y[', k, ']=', y[k])
    return y


def criaMatrixVandermonde(N):
    # Usado para criar a matriz vandermonde
    y = [0] * N
    for k in range(0, N, 1):
        y[k] = k+1
    x = np.array(y)
    v = np.vander(x, N)
    # Inverte as colunas
    v = np.fliplr(v)
    return v
# --------------------------------------------------------------------------------
# Calcula polinômio
# --------------------------------------------------------------------------------


def Polinomio(magic_ishort, sigfig):
    imprimeQuestao(
        6, 'Queremos encontrar um polinômio de grau  n>0 pn(x)=a0 + a1x + a2x^2 + ...+anx^n')

    # Resposta
    imprimeTitulo('Resposta')
    # p5(x) = a0 + a1x + a2x^2 + a3x^3 + a4x^4 + a5x^5
    # p5(xk) = yk

    # y0 = a0 +a1X0 + a2X0^2 + a3X0^3 + a4X0^4 + a5X0^5
    # y1 = a0 +a1X1 + a2X1^2 + a3X1^3 + a4X1^4 + a5X1^5
    # y2 = a0 +a1X2 + a2X2^2 + a3X2^3 + a4X2^4 + a5X2^5
    # y3 = a0 +a1X3 + a2X3^2 + a3X3^3 + a4X3^4 + a5X3^5
    # y4 = a0 +a1X4 + a2X4^2 + a3X4^3 + a4X4^4 + a5X4^5
    # y5 = a0 +a1X5 + a2X5^2 + a3X5^3 + a4X5^4 + a5X5^5

    # [1 X0 X0^2 X0^3 X0^4 X0^5 X0^6]    [a0]    [y0]
    # [1 X1 X1^2 X1^3 X1^4 X1^5 X1^6]    [a1]    [y1]
    # [1 X2 X2^2 X2^3 X2^4 X2^5 X2^6] x  [a2] =  [y2]
    # [1 X3 X3^2 X3^3 X3^4 X3^5 X3^6]    [a3]    [y3]
    # [1 X4 X4^2 X4^3 X4^4 X4^5 X4^6]    [a4]    [y4]
    # [1 X5 X5^2 X5^3 X5^4 X5^5 X5^6]    [a5]    [y5]
    # [1 X6 X6^2 X6^3 X6^4 X6^5 X6^6]    [a6]    [y6]

    # x0 = 1 => y0 = -11
    # x1 = 2 => y1 = -320
    # x2 = 3 => y2 = -2187
    # x3 = 4 => y3 = -8192
    # x4 = 5 => y4 = -21875
    # x5 = 6 => y5 = -46656

    # -11    = a0 + a1*(1) + a2*(1)^2 + a3*(1)^3 + a4*(1)^4 + a5*(1)^5 + a6*(1)^6
    # -320   = a0 + a1*(2) + a2*(2)^2 + a3*(2)^3 + a4*(2)^4 + a5*(2)^5 + a6*(2)^6
    # -2187  = a0 + a1*(3) + a2*(3)^2 + a3*(3)^3 + a4*(3)^4 + a5*(3)^5 + a6*(3)^6
    # -8192  = a0 + a1*(4) + a2*(4)^2 + a3*(4)^3 + a4*(4)^4 + a5*(4)^5 + a6*(4)^6
    # -21875 = a0 + a1*(5) + a2*(5)^2 + a3*(5)^3 + a4*(5)^4 + a5*(5)^5 + a6*(5)^6
    # -46656 = a0 + a1*(6) + a2*(6)^2 + a3*(6)^3 + a4*(6)^4 + a5*(6)^5 + a6*(6)^6

    # -11    = a0 +  a1*1 +  a2*1  + a3*1   + a4*1   + a5*1    + a6*1             [  1   1   1   1   1]     [a0]    [-123045067]
    # -320   = a0 +  a1*2 +  a2*4  + a3*8   + a4*16  + a5*32   + a6*(1)             [  1   2   4   8  16]     [a1]    [-3937442112]
    # -2187  = a0 +  a1*3 +  a2*9  + a3*27  + a4*81  + a5*243  + a6*(1)       =>    [  1   3   9  27  81] *   [a2] =  [-29899950795]
    # -8192  = a0 +  a1*4 +  a2*16 + a3*64  + a4*256 + a5*1024 + a6*(1)             [  1   4  16  64 256]     [a3]    [-125998145536]
    # -21875 = a0 +  a1*5 +  a2*25 + a3*125 + a4*625 + a5*3125 + a6*(1)             [  1   5  25 125 625]     [a4]    [-384515821875]
    # -46656 = a0 +  a1*5 +  a2*25 + a3*125 + a4*625 + a5*3125 + a6*(1)             [  1   5  25 125 625]     [a4]    [-384515821875]

    N = 5
    y = GeraArrayRespostas(N+1, magic_ishort)
    imprimeTitulo('Vetor Resposta y')
    print(y)
    v = criaMatrixVandermonde(N+1)
    imprimeTitulo('Matriz de Vandermonde')
    print(v)
    # Criando a matrix extendida com Vandermond e o resultado de y
    a = np.c_[v, y]
    imprimeTitulo('Matriz Vandermonde extendida com resposta Y')
    print(a)
    # Usando Gauss para resolver
    x_vet = elim_gauss_pivot_parcial_precisao_reduzida(a, sigfig)

    imprimeTitulo('Vetor Resposta')
    print(x_vet)

    input("Press Enter to continue...")


# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def TarefaFinal(titulo, nusp):
    LimpaTela()
    imprimeTitulo(titulo)

    # ----------------------------------------------------------------------------
    # Imprime mágic Number
    # ----------------------------------------------------------------------------
    print("nusp  =", nusp)
    magic_ilong, magic_ishort = MagicNumbers(nusp)
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)
    # for sigfig in ()
    Polinomio(magic_ishort, 14)

    imprimeTraco(180)
    input("Press Enter to continue...")
