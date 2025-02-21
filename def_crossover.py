import random

def crossover_um_ponto(populacao):
    nova_populacao = []
    for i in range(0, len(populacao), 2):
        pai1 = populacao[i]
        pai2 = populacao[i + 1]

        ponto_corte = random.randint(1, len(pai1[1]) - 1)

        # Filho 1: primeira parte do pai1 + segunda parte do pai2
        filho1 = (pai1[0], pai1[1][:ponto_corte] + pai2[1][ponto_corte:])
        
        # Filho 2: primeira parte do pai2 + segunda parte do pai1
        filho2 = (pai2[0], pai2[1][:ponto_corte] + pai1[1][ponto_corte:])

        nova_populacao.extend([filho1, filho2])
    return nova_populacao

def crossover_dois_pontos(populacao):
    nova_populacao = []
    for i in range(0, len(populacao), 2):
        pai1 = populacao[i]
        pai2 = populacao[i+1]

        if len(pai1[1]) < 2:
            nova_populacao.extend([pai1, pai2])
            continue

        ponto_corte1 = random.randint(1, len(pai1[1])-1)
        ponto_corte2 = random.randint(ponto_corte1, len(pai1[1])-1)

        filho1 = (pai1[0], pai1[1][:ponto_corte1] + pai2[1][ponto_corte1:ponto_corte2] + pai1[1][ponto_corte2:])
        filho2 = (pai2[0], pai2[1][:ponto_corte1] + pai1[1][ponto_corte1:ponto_corte2] + pai2[1][ponto_corte2:])
        
        nova_populacao.extend([filho1, filho2])
    return nova_populacao


def crossover_uniforme(populacao):
    nova_populacao = []
    for i in range(0, len(populacao), 2):
        pai1 = populacao[i]
        pai2 = populacao[i + 1]

        filho1_genes = []
        filho2_genes = []
        for j in range(len(pai1[1])):
            if random.random() < 0.5:
                filho1_genes.append(pai1[1][j])
                filho2_genes.append(pai2[1][j])
            else:
                filho1_genes.append(pai2[1][j])
                filho2_genes.append(pai1[1][j])

        filho1 = (pai1[0], tuple(filho1_genes))
        filho2 = (pai2[0], tuple(filho2_genes))

        nova_populacao.extend([filho1, filho2])
    return nova_populacao
