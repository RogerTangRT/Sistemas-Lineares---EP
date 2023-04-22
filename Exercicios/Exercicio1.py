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
    magic_ilong, magic_ishort = MagicNumbers(nusp)
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)

    imprimeQuestao(
        1, 'Qual o maior número positivo que podemos representar em inteiros com sinal se tivermos uma representação com magic_ishort bits? Justifique.')
    # Resposta
    imprimeTitulo('Resposta')
    print('magic_ishort:', end='')
    print(magic_ishort)
    print('Usando a representação de (Sign-Magnitude) Os valores vão de:', -(2**(magic_ishort-1) -
          1), ' até ', 2**(magic_ishort-1)-1)
    print('Usando a representação de (Complement-Magnitude) Os valores vão de:', -
          (2**(magic_ishort-1)), ' até ', 2**(magic_ishort-1)-1)
    print('Como temos que reservar um bit para o sinal (sign bit) nos resta apenas ' +
          str(magic_ishort - 1) + ' bits para representarmos o número (magnitude bits).')
    valor = 2**(magic_ishort - 1)
    print(
        'Temos que o valor máximo representado por 12 bits com sinal é de [** ', 2**(magic_ishort-1)-1, ' **]')
    print('Observação: Complement-Magnitude permite a representação de um número a mais por conta de usar o "-0" como um valor negativo adicional')
    imprimeTraco(180)
    input("Press Enter to continue...")
