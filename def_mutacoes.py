import random

def swap(individuo, p=0.1):
    '''
    promove mutação em uma população trocando a posição de dois elementos
    @param individuo: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    nova_individuo = []
    for i in range(len(individuo)):
        if random.random() < p:
            nova_individuo.append((individuo[i][0],(individuo[i][1][1], individuo[i][1][0])))
        else:
            nova_individuo.append((individuo[i][0], individuo[i][1]))
    return nova_individuo

def novo_valor(individuo, p=0.1):
    '''
    promove mutação em uma população trocando o valor de um elemento
    @param individuo: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    nova_individuo = []
    coordenada_trocada = random.randint(0, 1)
    for i in range(len(individuo)):
        if random.random() < p:
            nova_coordenada = list(individuo[i][1])
            nova_coordenada[coordenada_trocada] = random.randint(0, 30)
            nova_individuo.append((individuo[i][0], tuple(nova_coordenada)))
        else:
            nova_individuo.append((individuo[i][0], individuo[i][1]))
    
    return nova_individuo

def mutacao_swap(populacao, p=0.1):
    '''
    promove mutação em uma população trocando a posição de dois elementos
    @param populacao: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    nova_populacao = []
    for individuo in populacao:
        nova_populacao.append(swap(individuo, p))
    return nova_populacao

def mutacao_novo_valor(populacao, p=0.1):
    '''
    promove mutação em uma população trocando o valor de um elemento
    @param populacao: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    nova_populacao = []
    for individuo in populacao:
        nova_populacao.append(novo_valor(individuo, p))
    return nova_populacao