'''
Parte 1: Variação do Parâmetro de Seleção
O propósito deste experimento é intuir se alguma das funções de seleção que você
implementou tem impacto na performance dos algoritmos.
Escolha duas variações de algoritmos genéticos entre as implementadas para as
quais as funções de emparelhamento (seleção) são diferentes, mas todas as outras
partes dos algoritmos são iguais.
Gere uma entrada aleatória de tamanho 10 e execute cada uma das variações selecionadas
para esta entrada.
Repita 20 vezes, anotando a cada execução de algoritmo qual foi o indivíduo mais
apto encontrado por cada variação e o seu valor de fitness.
Analise os números encontrados e busque identificar qual destas duas variações se
mostrou melhor que a outra.
'''
from def_matrizes import gerar_populacao, gerar_instalacoes, gerar_locais, gerar_matrizes
from algoritmo import algoritmo_genetico, lista_fitness
from def_selecao import selecao_roleta, selecao_torneio
from def_elitismos import elitismo_simples, elitismo_composto
from def_mutacoes import mutacao_swap, mutacao_reverso
from def_crossover import crossover_um_ponto, crossover_dois_pontos

def main():
    for i in range(20):
        #Versão 1: Seleção por Roleta	

        n = 10
        num_geracoes = 5
        # Gera locais fixos e instalações
        locais_fixos = gerar_locais(n)
        instalacoes = gerar_instalacoes(n)

        # Gera população inicial
        populacao = gerar_populacao(n, instalacoes, locais_fixos)
        matriz_distancia, matriz_fluxo = gerar_matrizes(locais_fixos, instalacoes)

        # Executa o algoritmo genético com seleção por Roleta
        print("\nExecutando algoritmo genético com seleção por Roleta...")
        populacao_roleta = algoritmo_genetico(populacao, num_geracoes, lista_fitness, selecao_roleta, crossover_um_ponto, elitismo_simples, mutacao_swap,locais_fixos, matriz_distancia, matriz_fluxo)
        fitness_final = lista_fitness(populacao_roleta, locais_fixos, matriz_distancia, matriz_fluxo)
        print("Exibindo o melhor indivíduo encontrado e seu fitness:")
        print(f"Melhor indivíduo: {populacao_roleta[0]}")
        print(f"Fitness: {fitness_final[0]}")

        # Versão 2: Seleção por Torneio
        print("\nExecutando algoritmo genético com seleção por Torneio...")
        populacao_torneio = algoritmo_genetico(populacao, num_geracoes, lista_fitness, selecao_torneio, crossover_um_ponto, elitismo_simples, mutacao_swap, locais_fixos, matriz_distancia, matriz_fluxo)
        fitness_final = lista_fitness(populacao_torneio, locais_fixos, matriz_distancia, matriz_fluxo)
        print("Exibindo o melhor indivíduo encontrado e seu fitness:")
        print(f"Melhor indivíduo: {populacao_torneio[0]}")
        print(f"Fitness: {fitness_final[0]}")

if __name__ == "__main__":
    main()