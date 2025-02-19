'''
A técnica de Algoritmos Genéticos permite ampla variação nas implementação de funções
de emparelhamento, crossover, fitness, elitismo e mutação, entre outras possibilidades.
Para este projeto, você deve propor variações de algoritmos genéticos contemplando
pelo menos:
1. duas formas diferentes de emparelhamento dos indivíduos (seleção)
2. duas formas diferentes de efetuar o crossover (reprodução)
3. duas formas diferentes de promover elitismo entre gerações
4. duas formas diferentes de promover mutação
As suas escolhas para cada parte desses algoritmos devem ser discutidas no relatório
que acompanhará a entrega dos códigos. Quais foram as suas intuições? Por que decidiram
por estas formas de implementar cada aspecto dos algoritmos genéticos?
No total, as combinações dessas escolhas lhe dará um conjunto de 16 algoritmos
genéticos diferentes, sem contar a possibilidade de varias os parâmetros como tamanho
das gerações, critério de parada, taxas de elitismo e mutação...
A próxima sessão lhe pedirá para escolher algumas variações por vez para realizar
experimentos com entradas aleatórias, de forma que cada comparação vá ser feita entre
duas a quatro variações dos algoritmos.
'''

from def_matrizes import gerar_matrizes
import random

#Definindo de forma geral a estrutura de um algoritmo genético
#Passaremos por parâmetro a matriz de distâncias, a matriz de fluxo, o tamanho da população, o número de gerações, a função de fitness, a função de seleção, a função de crossover, a função de elitismo e a função de mutação

def algoritmo_genetico(matriz_distancia, matriz_fluxo, tamanho_populacao, num_geracoes, fitness, selecao, crossover, elitismo, mutacao):
    populacao = gerar_populacao(matriz_distancia, matriz_fluxo, tamanho_populacao)
    for i in range(num_geracoes):
        populacao = selecao(populacao, fitness)
        populacao = crossover(populacao)
        populacao = elitismo(populacao, fitness)
        populacao = mutacao(populacao)
    return populacao

#Função para gerar a população inicial
def gerar_populacao(matriz_distancia, matriz_fluxo, tamanho_populacao):
    populacao = gerar_matrizes    

#Função de fitness
def fitness(populacao):
    return populacao

#Função de seleção
def selecao(populacao, fitness):
    return populacao

#Função de crossover
def crossover(populacao):
    return populacao

#Função de elitismo
def elitismo(populacao, fitness):
    return populacao

#Função de mutação
def mutacao(populacao):
    return populacao

if __name__ == '__main__':
    n = 5
    matriz_distancia, matriz_fluxo = gerar_matrizes(n)
    tamanho_populacao = 10
    num_geracoes = 10
    algoritmo_genetico(matriz_distancia, matriz_fluxo, tamanho_populacao, num_geracoes, fitness, selecao, crossover, elitismo, mutacao)
    

