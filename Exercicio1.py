from Auxiliares import *
# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def Exercicio1(titulo, nusp):
    imprimeTitulo(titulo)

    # ----------------------------------------------------------------------------
    # Imprime mágic Number
    # ----------------------------------------------------------------------------
    print("nusp  =", nusp)
    magic_ilong = int(str(nusp).replace("0", ""))
    magic_ishort = int(str(magic_ilong)[:2])
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)

    imprimeQuestao(
        1, 'Qual o maior número positivo que podemos representar em inteiros com sinal se tivermos uma representação com magic_ishort bits? Justifique.')
    # Resposta
    imprimeTitulo('Resposta')
    print('magic_ishort:', end='')
    print(magic_ishort)
    print('Como temos que reservar um bit para o sinal nos resta apenas ' +
          str(magic_ishort - 1) + ' bits para representarmos o número.')
    valor = 2**(magic_ishort - 1)
    print('Entáo é possível representar até ' + str(valor) + ' números')
    print('Como os valores numéricos se iniciam em 0, entáo temos que o valor máximo representado por 12 bits com sinal é de ' + str(valor-1))
    imprimeTraco(100)
