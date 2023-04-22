# --------------------------------------------------------------------------------
# Imprime Título com traçaos antes de depois do tamanho do título
# --------------------------------------------------------------------------------
def imprimeTitulo(titulo):
    print('-'*len(titulo))
    print(titulo)
    print('-'*len(titulo))


def imprimeQuestao(numeroQuestao, titulo):
    tamanhoTraco = len('Questão ') + \
        len(str(numeroQuestao))+len(':')+len(titulo) + 1
    print('-'*tamanhoTraco)
    print('Questão ' + str(numeroQuestao) + ':', titulo)
    print('-'*tamanhoTraco)

# --------------------------------------------------------------------------------
# Imprime Traço duplo
# --------------------------------------------------------------------------------


def imprimeTraco(tamanho):
    print('='*tamanho)
