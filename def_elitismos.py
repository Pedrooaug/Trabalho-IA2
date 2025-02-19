import random

def elitismo_simples(populacao, fitness):
    '''
    faz uma seleção ordenada pelo fitness onde metade da população atual vai
    para a próxima geração
    @param populacao: lista de individuos com o formato [coordenadas, objeto alocado]
    @param fitness: lista de valores de fitness para cada individuo
    @return: lista de individuos selecionados
    '''
    populacao.sort(key=lambda x: fitness[x[1]])
    return populacao[:len(populacao)//2]

def elitismo_composto(populacao, fitness):
    '''
    faz uma seleção ordenada mei doida onde metade da população atual vai
    para a próxima geração
    serão selecionados metade da população, dessa forma:
    - 1/4 dos melhores
    - 1/4 aleatórios, podendo ser dos piores ou melhores
    sem elementos repetidos
    @param populacao: lista de individuos com o formato [coordenadas, objeto alocado]
    @param fitness: lista de valores de fitness para cada individuo
    @return: lista de individuos selecionados
    '''
    populacao.sort(key=lambda x: fitness[x[1]])
    metade = len(populacao)//2
    melhores = populacao[:metade//2]
    selecionados = set(melhores)
    while len(selecionados) < metade:
        selecionados.add(random.choice(populacao)[1])
    return [populacao[i] for i in selecionados]