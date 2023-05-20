from Auxiliares import LimpaTela
from EliminacaoGaussiana.decomposicao_Doolittle_LU import LUDecompDoolittle
from Teoria.AritimeticaPontoFlutuante import AritimeticaPontoFlutuante
from Teoria.NumerosReaisComputador import NumerosReaisNoComputador
from Exercicios.EliminacaoGaussiana import EliminacaoGaussiana
from Exercicios.Exercicio1 import Exercicio1
from Exercicios.Exercicio2 import Exercicio2
from Exercicios.Exercicio3 import Exercicio3
from Exercicios.Exercicio4 import Exercicio4
from Exercicios.Exercicio5 import Exercicio5
from Exercicios.TarefaFinal import TarefaFinal
import numpy as np
import matplotlib.pyplot as plt


# Coloque aqui o seu número USP
nusp = 12553156
LimpaTela()

# data to be plotted
#x = np.arange(1, 11)
#sifig4 = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
#sifig5 = np.array([100, 210, 300, 420, 500, 600, 700, 800, 900, 1000])

# plotting
#plt.title("Comparação dos graph")
#plt.xlabel("X sigfig ")
#plt.ylabel("Y valor => 1")
#plt.plot(x, sifig4, color="green", label='sigfig4')
#plt.plot(x, sifig5, color="red", label='sigfig5')
# plt.legend()
# plt.show()


# AritimeticaPontoFlutuante()
# Exercicio1('Exercicio 1', nusp)
# NumerosReaisNoComputador()
# Exercicio2('Exercicio 2', nusp)
# Exercicio3('Exercicio 3', nusp)
# EliminacaoGaussiana('Eliminação Guassiana', nusp)
#Exercicio4('Exercicio 4', nusp)
#Exercicio5('Exercicio 5', nusp)
#TarefaFinal('Tarefa Final', nusp)

# Driver code
#  2x - y -2z
# -4x +6y +3z
# -4x -2y +8z
a = np.array([[2, -1, -2], [-4, 6, 3],  [-4, -2, 8]])

LUDecompDoolittle(a)
