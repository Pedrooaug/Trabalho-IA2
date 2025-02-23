import random
from def_elitismos import elitismo_simples, elitismo_composto
from def_mutacoes import mutacao_swap, mutacao_novo_valor
from def_selecao import selecao_roleta, selecao_torneio
from def_crossover import crossover_um_ponto, crossover_dois_pontos
from def_matrizes import gerar_populacao, gerar_instalacoes, gerar_locais, gerar_matrizes
from algoritmo import lista_fitness, algoritmo_genetico

def main():
    n = 5
    # Gera locais fixos e instalações UMA ÚNICA VEZ
    locais_fixos = gerar_locais(n)
    instalacoes = gerar_instalacoes(n)
    
    # Gera população com os mesmos locais_fixos e instalações
    populacao = gerar_populacao(n, instalacoes, locais_fixos)
    
    # Gera matrizes com os mesmos locais_fixos e instalações
    matriz_distancia, matriz_fluxo = gerar_matrizes(locais_fixos, instalacoes)
    
    # Testes
    print("População:")
    for i, individuo in enumerate(populacao):
        print(f'Indivíduo {i}: {individuo}')
    
    print("\nMatriz de distância:")
    for linha in matriz_distancia:
        print(linha)
    
    print("\nMatriz de fluxo:")
    for linha in matriz_fluxo:
        print(linha)
    
    # Testa o fitness dos indivíduos
    fitness_populacao = lista_fitness(populacao, locais_fixos, matriz_distancia, matriz_fluxo)
    for i, individuo in enumerate(populacao):
        print(f'Fitness do indivíduo {i} :{individuo} => {fitness_populacao[i]}')

    # Teste da Seleção por Roleta
    print("\nSeleção por Roleta:")
    selecionados_roleta = selecao_roleta(populacao, fitness_populacao)
    for i, individuo in enumerate(selecionados_roleta):
        print(f'Indivíduo {i}: {individuo}')

    # Teste da Seleção por Torneio
    print("\nSeleção por Torneio:")
    selecionados_torneio = selecao_torneio(populacao, fitness_populacao)
    for i, individuo in enumerate(selecionados_torneio):
        print(f'Indivíduo {i}: {individuo}')
    
    # Teste do Crossover de um ponto
    print("\nCrossover de um ponto:")
    filhos_um_ponto = crossover_um_ponto(selecionados_roleta)
    for i, filho in enumerate(filhos_um_ponto):
        print(f'Filho {i}: {filho}')


    # Teste do Crossover de dois pontos
    print("\nCrossover de dois pontos:")
    filhos_dois_pontos = crossover_dois_pontos(selecionados_roleta)
    for i, filho in enumerate(filhos_dois_pontos):
        print(f'Filho {i}: {filho}')

    # Teste da Mutação Swap
    print("\nMutação Swap:")
    filhos_mutados_swap = mutacao_swap(filhos_um_ponto)
    for i, filho in enumerate(filhos_mutados_swap):
        print(f'Filho {i}: {filho}')

    # Teste da Mutação Novo Valor
    print("\nMutação Novo Valor:")
    filhos_mutados_novo_valor = mutacao_novo_valor(filhos_um_ponto)
    for i, filho in enumerate(filhos_mutados_novo_valor):
        print(f'Filho {i}: {filho}')


    # Teste do Elitismo Simples
    print("\nElitismo Simples:")
    populacao_elitismo_simples = elitismo_simples(filhos_mutados_novo_valor, fitness_populacao)
    for i, individuo in enumerate(populacao_elitismo_simples):
        print(f'Indivíduo {i}: {individuo}')

    # Teste do Elitismo Composto
    print("\nElitismo Composto:")
    populacao_elitismo_composto = elitismo_composto(filhos_mutados_novo_valor, fitness_populacao)
    for i, individuo in enumerate(populacao_elitismo_composto):
        print(f'Indivíduo {i}: {individuo}')
    
    
    # Teste do Algoritmo Genético
    print("\nAlgoritmo Genético:")
    n_geracoes = 5
    populacao_final = algoritmo_genetico(populacao, n_geracoes, fitness_populacao, selecao_roleta, crossover_um_ponto, elitismo_simples, mutacao_swap)
    for i, individuo in enumerate(populacao_final):
        print(f'Indivíduo {i}: {individuo}')

if __name__ == "__main__":
    main()