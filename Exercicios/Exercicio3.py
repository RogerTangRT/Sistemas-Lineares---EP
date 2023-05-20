
import sys
from Auxiliares import *


# --------------------------------------------------------------------------------
# Questao 3.1
# --------------------------------------------------------------------------------


def Questao31(nusp):
    imprimeQuestao(
        3.1, 'Quantos algarismos significativos são necessários para representar o seu número USP na forma de um float em base 10? Justifique')
    # Resposta
    imprimeTitulo('Resposta')
    # São necessário 9 algarismos
    # 0.123045068 x 10^9 =>  Pela representaçãp 0,AAAAA... x 10^B seria necessário 9 dígitos
    print(0.12553156 * 10**-8)
    print('São necessário 8 algarismos')
    print('0.12553156 x 10^8 =>  Pela representaçãp 0,AAAAA... x 10^B seria necessário 8 dígitos')
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 3.2
# --------------------------------------------------------------------------------


def Questao32(nusp):
    imprimeQuestao(
        3.2, 'Divida o seu número USP por 17. Represente o número resultante com aritmética de ponto flutuante com 5 algarismos significativos na base 10, arredondando se necessário.')
    # Para saber esse número de algarismos (dígitos) significativos na sua máquina, use:
    imprimeTitulo('Algarismos significativos da máquina')
    print('sys.float_info.dig:', sys.float_info.dig)
    # Resposta
    imprimeTitulo('Resposta')
    print('nusp/17: ', nusp/17)
    print('nusp 123045068 / 17 =  738.420,9411764706')
    print(0.73842 * 10**6)
    print('Representação com ponto flutuante de 5 algarismos: 0.73842 x 10^1 = 7.237.900')
    print('nusp 123045068 / 17 =  7.237.900')
    print('Por conta de usar apenas 5 digitos perde-se precisão do número')

    # nusp 123045068 / 17 =  7.237.945,176470588
    #                        7.237.900
    # Representação com ponto flutuante de 5 algarismos: 0.72379 x 10^2 = 7.237.900
    # Por conta de usar apenas 5 digitos perde-se precisão do número

# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def Exercicio3(titulo, nusp):
    LimpaTela()
    imprimeTitulo(titulo)

    # ----------------------------------------------------------------------------
    # Imprime mágic Number
    # ----------------------------------------------------------------------------
    print("nusp  =", nusp)
    magic_ilong, magic_ishort = MagicNumbers(nusp)
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)

    Questao31(nusp)
    Questao32(nusp)

    imprimeTraco(180)
    input("Press Enter to continue...")
