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

from def_matrizes import gerar_matrizes, gerar_populacao, gerar_locais, gerar_instalacoes
from def_crossover import crossover_um_ponto, crossover_dois_pontos
from def_selecao import selecao_roleta, selecao_torneio
from def_elitismos import elitismo_simples, elitismo_composto
from def_mutacoes import mutacao_swap, mutacao_reverso
import random

#Definindo de forma geral a estrutura de um algoritmo genético
#Passaremos por parâmetro a matriz de distâncias, a matriz de fluxo, a população, o número de gerações, a função de fitness, a função de seleção, a função de crossover, a função de elitismo e a função de mutação
#A estrutura do algoritmo é baseada na chamada das funções passadas por parâmetro, sendo elas o crossover, a seleção, a mutação e o elitismo


def algoritmo_genetico(populacao, n_geracoes, gerar_fitness, selecao, crossover, elitismo, mutacao, locais_fixos, matriz_distancia, matriz_fluxo):
    sobreviventes = []
    for i in range(n_geracoes):
        # Seleciona os indivíduos para reprodução
        fitness = gerar_fitness(populacao, locais_fixos, matriz_distancia, matriz_fluxo)
        selecionados = selecao(populacao, fitness)
        
        # Realiza o crossover
        filhos = crossover(selecionados)
        
        # Adiciona os filhos aos sobreviventes, compondo a nova população com o tamanho da população inicial
        n = sobreviventes + filhos
        novos = n[:len(populacao)]

        # Realiza a mutação
        filhos_mutados = mutacao(novos)
        populacao = filhos_mutados
        print(f"Geração {i}:")
        for j, individuo in enumerate(populacao):

            print(f'Indivíduo {j}: {individuo}, fitness: {fitness[j]}')

        
        # Realiza o elitismo
        sobreviventes = elitismo(populacao, filhos_mutados)

    return populacao

def gerar_instalacoes2(individuo):
    return [instalacao for instalacao, local in individuo]

#Função de fitness
#O fitness é calculado como a multiplicação do valor da matriz de distância pelo valor da matriz de fluxo do indivíduo
#Para isso, precisamos encontrar o índice de cada indivíduo na matriz de distância e na matriz de fluxo
#Para facilitar, as matrizes são simétricas, então podemos procurar apenas na metade superior da matriz
#Passo a passo:
#1. Encontrar o índice do indivíduo na matriz de distância
#2. Encontrar o índice do indivíduo na matriz de fluxo
#3. Multiplicar os valores das duas matrizes
def fitness(individuo, locais_fixos, matriz_distancia, matriz_fluxo):
    custo = 0
    n = len(individuo)
    instalacoes = gerar_instalacoes2(individuo)
    # Cria um dicionário para mapear instalações para seus locais no indivíduo
    mapa = {obj: idx_local for obj, idx_local in individuo}
    
    for i in range(n):
        for j in range(i + 1, n):
            # Obtém os índices dos locais das instalações i e j
            local_i = locais_fixos.index(mapa[instalacoes[i]])
            local_j = locais_fixos.index(mapa[instalacoes[j]])
            
            # Calcula o custo para o par (i, j)
            custo += matriz_fluxo[i][j] * matriz_distancia[local_i][local_j]
    
    return custo

#Retornando o fitness como lista 
def lista_fitness(populacao, locais_fixos, matriz_distancia, matriz_fluxo):
    fitness_populacao = []
    for i in range(len(populacao)):
        fitness_populacao.append(fitness(populacao[i], locais_fixos, matriz_distancia, matriz_fluxo))
    return fitness_populacao

def main():
    n = 10
    # Gera locais fixos e instalações UMA ÚNICA VEZ
    locais_fixos = gerar_locais(n)
    instalacoes = gerar_instalacoes(n)
    
    # Gera população com os mesmos locais_fixos e instalações
    populacao = gerar_populacao(n, instalacoes, locais_fixos)
    
    # Gera matrizes com os mesmos locais_fixos e instalações
    matriz_distancia, matriz_fluxo = gerar_matrizes(locais_fixos, instalacoes)
    
    # Testes
    print("Indivíduos:")
    for i, individuo in enumerate(populacao):
        print(f'Indivíduo {i}: {individuo}')
    
    #print("\nMatriz de distância:")
    #for linha in matriz_distancia:
        #print(linha)
    
    #print("\nMatriz de fluxo:")
    #for linha in matriz_fluxo:
        #print(linha)
    
    # Testa o fitness dos indivíduos
    #for i, individuo in enumerate(populacao):
        #print(f'Fitness do indivíduo {individuo}: {fitness(individuo, locais_fixos, matriz_distancia, matriz_fluxo)}')

    # Testa o algoritmo genetico
    n_geracoes = 10

    sobreviventes = algoritmo_genetico(populacao, n_geracoes, lista_fitness, selecao_roleta, crossover_um_ponto, elitismo_simples, mutacao_swap, locais_fixos, matriz_distancia, matriz_fluxo)
    print("\nSobreviventes:")
    for i, individuo in enumerate(sobreviventes):
        print(f'Indivíduo {i}: {individuo}')
    print("\nFitness dos sobreviventes:")
    lista_fitness_sobreviventes = lista_fitness(sobreviventes, locais_fixos, matriz_distancia, matriz_fluxo)
    for i, fitness in enumerate(lista_fitness_sobreviventes):
        print(f'Fitness do indivíduo {i}: {fitness}')

if __name__ == '__main__':
    main()    