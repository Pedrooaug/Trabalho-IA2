import random
from def_elitismos import elitismo_simples
from def_selecao import selecao_roleta, selecao_torneio
from def_crossover import crossover_um_ponto, crossover_dois_pontos, crossover_uniforme, crossover_aritmetico

# Crossover uniforme 
# Crossover de um ponto

def main():
    populacao = [
        ("Ind1", (1, 2)),
        ("Ind2", (3, 5)),
        ("Ind3", (5, 6)),
        ("Ind4", (7, 8)),
        ("Ins5", (6, 9))
    ]

    fitness = [0.1, 0.3, 0.2, 0.4, 0.4]  

    print("População Inicial:")
    for ind in populacao:
        print(ind)

    print("\nFitness da População:")
    for i, ind in enumerate(populacao):
        print(f"{ind} -> Fitness: {fitness[i]}")

    # Teste da Seleção por Roleta
    populacao_selecionada_roleta = selecao_roleta(populacao, fitness)
    print("\nPopulação após Seleção por Roleta:")
    for ind in populacao_selecionada_roleta:
        print(ind)

    # Teste da Seleção por Torneio
    populacao_selecionada_torneio = selecao_torneio(populacao, fitness, k=2)
    print("\nPopulação após Seleção por Torneio:")
    for ind in populacao_selecionada_torneio:
        print(ind)

    # Teste do Crossover de Um Ponto
    populacao_crossover_um_ponto = crossover_um_ponto(populacao_selecionada_roleta)
    print("\nPopulação após Crossover de Um Ponto:")
    for ind in populacao_crossover_um_ponto:
        print(ind)

    # Teste do Crossover Uniforme
    populacao_crossover_dois_pontos = crossover_dois_pontos(populacao_selecionada_torneio)
    print("\nPopulação após Crossover de Dois Pontos:")
    for ind in populacao_crossover_dois_pontos:
        print(ind)

    # Teste do Crossover Uniforme
    populacao_crossover_uniforme = crossover_uniforme(populacao)
    print("\nPopulação após Crossover Uniforme:")
    for ind in populacao_crossover_uniforme:
        print(ind)

    # Teste do Crossover Uniforme
    populacao_crossover_aritmetico = crossover_aritmetico(populacao)
    print("\nPopulação após Crossover Aritmético:")
    for ind in populacao_crossover_aritmetico:
        print(ind)

    # Teste do Elitismo Simples
    populacao_elitismo = elitismo_simples(populacao_crossover_um_ponto, fitness)
    print("\nPopulação após Elitismo Simples:")
    for ind in populacao_elitismo:
        print(ind)

if __name__ == "__main__":
    main()