import random

def crossover_um_ponto(populacao):
    nova_populacao = []
    
    for i in range(0, len(populacao) - 1, 2):  
        pai1 = populacao[i]
        pai2 = populacao[i + 1]

        ponto_corte = random.randint(1, len(pai1[1]) - 1)

        filho1 = (pai1[0], pai1[1][:ponto_corte] + pai2[1][ponto_corte:])
        
        filho2 = (pai2[0], pai2[1][:ponto_corte] + pai1[1][ponto_corte:])

        nova_populacao.extend([filho1, filho2])
    
    if len(populacao) % 2 != 0:
        nova_populacao.append(populacao[-1])
    
    return nova_populacao

def crossover_dois_pontos(populacao):
    nova_populacao = []
    for i in range(0, len(populacao), 2):  
        if i + 1 < len(populacao):  
            pai1 = populacao[i]
            pai2 = populacao[i + 1]

            if len(pai1[1]) < 2:
                nova_populacao.extend([pai1, pai2])
                continue

            ponto_corte1 = random.randint(1, len(pai1[1]) - 1)
            ponto_corte2 = random.randint(ponto_corte1, len(pai1[1]) - 1)

            filho1 = (pai1[0], pai1[1][:ponto_corte1] + pai2[1][ponto_corte1:ponto_corte2] + pai1[1][ponto_corte2:])
            filho2 = (pai2[0], pai2[1][:ponto_corte1] + pai1[1][ponto_corte1:ponto_corte2] + pai2[1][ponto_corte2:])
            
            nova_populacao.extend([filho1, filho2])
        else:
            nova_populacao.append(populacao[i])
    
    return nova_populacao
