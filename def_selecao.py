import random

def selecao_roleta(populacao, fitness):
    total_sum = sum(fitness)

    # Estou calculando a probabilidade de um indivíduo ser escolhido
    # a probabilidade de escolha deve ser proporcional ao fitness
    probabilidade_escolha = [f/total_sum for f in fitness]

    selecionados = random.choices(populacao, weights=probabilidade_escolha, k=len(populacao))

    return selecionados

def selecao_torneio(populacao, fitness, k=2):
    # k é a quantidade de competidores que vão participar do torneio, 
    # coloquei 3 só porque sim mesmo
    selecionados = []

    for _ in range(len(populacao)):
        competidores = random.sample(list(zip(populacao, fitness)), k)
        vencedor = max(competidores, key=lambda x: x[1])[0] # o vencedor é aquele com maior fitness
        selecionados.append(vencedor)
    return selecionados