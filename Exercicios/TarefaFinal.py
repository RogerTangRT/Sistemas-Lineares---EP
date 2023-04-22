from Auxiliares import *


def Polinomio(nusp):
    imprimeQuestao(
        6, 'Queremos encontrar um polinômio de grau  n>0 pn(x)=a0+a1x+a2x2+...+anxn')

    # Resposta
    imprimeTitulo('Resposta')
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
    magic_ilong = int(str(nusp).replace("0", ""))
    magic_ishort = int(str(magic_ilong)[:2])
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)
    Polinomio(nusp)

    imprimeTraco(180)
