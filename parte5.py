'''
Repita os passos abaixo para valores incrementais de n a partir de 10:
(a) Gere uma entrada aleatória de PQA com tamanho n
(b) Execute cada variação escolhida sobre essa entrada
(c) Anote o tempo que cada variação levo para concluir sua execução
Incremente n até que as variações do algoritmo comecem a demorar demais (de
acordo com a sua avaliação) para chegar a uma conclusão
'''

from def_matrizes import gerar_populacao, gerar_instalacoes, gerar_locais, gerar_matrizes
from algoritmo import algoritmo_genetico, lista_fitness
from def_selecao import selecao_roleta, selecao_torneio
from def_elitismos import elitismo_simples, elitismo_composto
from def_mutacoes import mutacao_swap, mutacao_reverso
from def_crossover import crossover_um_ponto, crossover_dois_pontos
import time

def main():
    for n in range(10, 1000, 100):
        # Gera locais fixos e instalações
        locais_fixos = gerar_locais(n)
        instalacoes = gerar_instalacoes(n)
        
        # Gera população com os mesmos locais_fixos e instalações
        populacao = gerar_populacao(n, instalacoes, locais_fixos)
        
        # Gera matrizes com os mesmos locais_fixos e instalações
        matriz_distancia, matriz_fluxo = gerar_matrizes(locais_fixos, instalacoes)
        
        # Testes
        print(f"População de tamanho {n}:")

        #Executando o algoritmo e marcando o tempo de execução
        start = time.time()
        fitness_pop = lista_fitness(populacao, locais_fixos, matriz_distancia, matriz_fluxo)
        print("Tempo de execução da lista de fitness: ", time.time() - start)
    
if __name__ == "__main__":
    main()