from Auxiliares import *
# --------------------------------------------------------------------------------
# MatematicaFurada
# --------------------------------------------------------------------------------


def MatematicaFurada():
    imprimeTitulo('Matemática Furada')
    a = 10
    b = 0.1
    c = 0.2

    r1 = a*(b + c)
    r2 = a*b + a*c
    print('r1 = a*(b + c)')
    print('r2 = a*b + a*c')

    print('Variáveis r1=' + str(r1) + ' e r2=' + str(r2))
    print('Valor calculado r1 == r2 => ', end='')
    print(r1 == r2)
    print('A distributiva e associatividade não valem no computador ?!?!')
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# SomaValoresFracionarios
# --------------------------------------------------------------------------------


def SomaValoresFracionarios():
    imprimeTitulo('Soma de Valores Fracionários')
    print('.2 + .2 + .2 == 0.6')
    print(.2 + .2 + .2 == 0.6)
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# SomaFracao
# --------------------------------------------------------------------------------


def SomaFracao():
    imprimeTitulo('Soma de Fraçao')
    sum = 0.0
    n = 10
    print('1/10 + 1/10 + ... 1/10 (10 vezes)')
    for i in range(n):
        sum += 1/n
    print('Resultado', sum)
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# NumerosInteirosNoComputador
# --------------------------------------------------------------------------------


def NumerosInteirosNoComputador():
    imprimeTitulo('Numeros Inteiros No Computador')
    print('Suponha que tenho apenas 3 bits para representar inteiros (ignore o sinal). ')
    print('Ou seja, temos os números binários 000, 001, 011, 100, 110, ..., 111 que representam respectivamente')
    print('0, 1, 2, 3, 4, 5, ..., 7 sendo 7 o maior número que conseguimos representar.')
    print('a=5 b=6')
    a = 5
    b = 6
    bin_a = bin(a)
    bin_b = bin(b)
    print('a:' + str(a), 'bin(a):' + str(bin_a))
    print('b:' + str(b), 'bin(b):' + str(bin_b))

    print('a+b:' + str(a+b), 'bin(a+b):' + bin(a+b))
    print('bin(a+b) -> 4 bits e não 3')
    input("Press Enter to continue...")
# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def AritimeticaPontoFlutuante():
    imprimeTitulo(' TEORIA - '+'Aritimetica de Ponto Flutuante')
    MatematicaFurada()
    SomaValoresFracionarios()
    SomaFracao()
    NumerosInteirosNoComputador()
    imprimeTraco(180)
