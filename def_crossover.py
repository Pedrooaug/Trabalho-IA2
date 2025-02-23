import random

def crossover_um_ponto(populacao):
    nova_populacao = []
    
    for i in range(0, len(populacao), 2):
        if i+1 >= len(populacao):
            nova_populacao.append(populacao[i])
            break

        pai1 = populacao[i]
        pai2 = populacao[i+1]

        ponto_de_corte = random.randint(1, len(pai1) - 1)

        filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:]
        filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:]

        nova_populacao.extend([filho1, filho2])
    
    return nova_populacao

def crossover_dois_pontos(populacao):
    nova_populacao = []
    for i in range(0, len(populacao), 2):  
        if i+1 >= len(populacao):
            nova_populacao.append(populacao[i])
            break

        pai1 = populacao[i]
        pai2 = populacao[i+1]

        ponto_de_corte1 = random.randint(1, len(pai1) - 2)
        ponto_de_corte2 = random.randint(ponto_de_corte1 + 1, len(pai1) - 1)

        filho1 = pai1[:ponto_de_corte1] + pai2[ponto_de_corte1:ponto_de_corte2] + pai1[ponto_de_corte2:]
        filho2 = pai2[:ponto_de_corte1] + pai1[ponto_de_corte1:ponto_de_corte2] + pai2[ponto_de_corte2:]

        nova_populacao.extend([filho1, filho2])
    
    return nova_populacao