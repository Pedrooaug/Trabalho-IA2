'''
Na Parte 2, escolha duas variações implementadas nas quais as funções de
crossover são diferentes, mas todas as outras partes dos algoritmos são iguais
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
        #Versão 1: Crossover de um ponto

        n = 10
        num_geracoes = 5
        # Gera locais fixos e instalações
        locais_fixos = gerar_locais(n)
        instalacoes = gerar_instalacoes(n)

        # Gera população inicial
        populacao = gerar_populacao(n, instalacoes, locais_fixos)
        matriz_distancia, matriz_fluxo = gerar_matrizes(locais_fixos, instalacoes)

        # Executa o algoritmo genético com crossover de um ponto
        print("\nExecutando algoritmo genético com crossover de um ponto...")
        populacao_um_ponto = algoritmo_genetico(populacao, num_geracoes, lista_fitness, selecao_roleta, crossover_um_ponto, elitismo_simples, mutacao_swap,locais_fixos, matriz_distancia, matriz_fluxo)
        fitness_final = lista_fitness(populacao_um_ponto, locais_fixos, matriz_distancia, matriz_fluxo)
        print("Exibindo o melhor indivíduo encontrado e seu fitness:")
        print(f"Melhor indivíduo: {populacao_um_ponto[0]}")
        print(f"Fitness: {fitness_final[0]}")

        # Versão 2: Crossover de dois pontos
        print("\nExecutando algoritmo genético com crossover de dois pontos...")
        populacao_dois_pontos = algoritmo_genetico(populacao, num_geracoes, lista_fitness, selecao_roleta, crossover_dois_pontos, elitismo_simples, mutacao_swap,locais_fixos, matriz_distancia, matriz_fluxo)
        fitness_final = lista_fitness(populacao_dois_pontos, locais_fixos, matriz_distancia, matriz_fluxo)
        print("Exibindo o melhor indivíduo encontrado e seu fitness:")
        print(f"Melhor indivíduo: {populacao_dois_pontos[0]}")
        print(f"Fitness: {fitness_final[0]}")

if __name__ == "__main__":
    main()