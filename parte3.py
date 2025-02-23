'''
Na Parte 3, escolha duas variações implementadas nas quais as funções elitismo
são diferentes, mas todas as outras partes dos algoritmos são iguais
'''
from def_matrizes import gerar_populacao, gerar_instalacoes, gerar_locais, gerar_matrizes
from algoritmo import algoritmo_genetico, lista_fitness
from def_selecao import selecao_roleta, selecao_torneio
from def_elitismos import elitismo_simples, elitismo_composto
from def_mutacoes import mutacao_swap, mutacao_reverso
from def_crossover import crossover_um_ponto, crossover_dois_pontos
from algoritmo import algoritmo_genetico, lista_fitness

def main():
    for i in range(20):
        #Versão 1: Elitismo Simples

        n = 10
        num_geracoes = 5
        # Gera locais fixos e instalações
        locais_fixos = gerar_locais(n)
        instalacoes = gerar_instalacoes(n)

        # Gera população inicial
        populacao = gerar_populacao(n, instalacoes, locais_fixos)
        matriz_distancia, matriz_fluxo = gerar_matrizes(locais_fixos, instalacoes)

        # Executa o algoritmo genético com elitismo simples
        fitness_pop = lista_fitness(populacao, locais_fixos, matriz_distancia, matriz_fluxo)
        print("\nExecutando algoritmo genético com elitismo simples...")
        populacao_simples = algoritmo_genetico(populacao, num_geracoes, fitness_pop, selecao_roleta, crossover_um_ponto, elitismo_simples, mutacao_swap)
        fitness_final = lista_fitness(populacao_simples, locais_fixos, matriz_distancia, matriz_fluxo)
        print("Exibindo o melhor indivíduo encontrado e seu fitness:")
        print(f"Melhor indivíduo: {populacao_simples[0]}")
        print(f"Fitness: {fitness_final[0]}")

        # Versão 2: Elitismo Composto
        print("\nExecutando algoritmo genético com elitismo composto...")
        populacao_composto = algoritmo_genetico(populacao, num_geracoes, fitness_pop, selecao_roleta, crossover_um_ponto, elitismo_composto, mutacao_swap)
        fitness_final = lista_fitness(populacao_composto, locais_fixos, matriz_distancia, matriz_fluxo)
        print("Exibindo o melhor indivíduo encontrado e seu fitness:")
        print(f"Melhor indivíduo: {populacao_composto[0]}")
        print(f"Fitness: {fitness_final[0]}")

if __name__ == "__main__":
    main()