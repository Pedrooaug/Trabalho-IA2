import random

def mutacao_swap(populacao, p=0.1):
    '''
    promove mutação em uma população trocando a posição de dois elementos
    @param populacao: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    nova_populacao = []
    for i in range(len(populacao)):
        if random.random() < p:
            nova_populacao.append((populacao[i][0],(populacao[i][1][1], populacao[i][1][0])))
        else:
            nova_populacao.append((populacao[i][0], populacao[i][1]))
    return nova_populacao

def mutacao_novo_valor(populacao, p=0.1):
    '''
    promove mutação em uma população trocando o valor de um elemento
    @param populacao: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    nova_populacao = []
    coordenada_trocada = random.randint(0, 1)
    for i in range(len(populacao)):
        if random.random() < p:
            nova_coordenada = list(populacao[i][1])
            nova_coordenada[coordenada_trocada] = random.randint(0, 30)
            nova_populacao.append(populacao[i][0], tuple(nova_coordenada))
        else:
            nova_populacao.append(populacao[i][0], populacao[i][1])