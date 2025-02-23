import random

def swap(individuo, p=0.1):
    '''
    promove mutação em uma população trocando a posição de dois elementos
    @param individuo: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    if random.random() < p:
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

def reverso(individuo, p=0.1):
    '''
    promove mutação em uma população trocando o valor de um elemento
    @param individuo: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    if random.random() < p:
        individuo = individuo[::-1]
    return individuo

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

def mutacao_reverso(populacao, p=0.1):
    '''
    promove mutação em uma população trocando o valor de um elemento
    @param populacao: lista de individuos com o formato [objeto alocado, coordenadas]
    @param p: probabilidade de mutação, valor entre 0 e 1
    @return: lista de individuos mutados
    '''
    nova_populacao = []
    for individuo in populacao:
        nova_populacao.append(reverso(individuo, p))
    return nova_populacao