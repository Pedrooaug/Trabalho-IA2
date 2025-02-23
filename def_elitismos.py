import random

def elitismo_simples(populacao, fitness):
    '''
    faz uma seleção ordenada pelo fitness onde metade da população atual vai
    para a próxima geração
    @param populacao: lista de individuos com o formato [objeto alocado, coordenadas]
    @param fitness: lista de valores de fitness para cada individuo
    @return: lista de individuos selecionados
    '''
    #selecionados = []
    #for individuo in populacao:
     #   selecionados.append(simples(individuo, fitness))
    #return selecionados
    zipado = list(zip(populacao, fitness)) # junta todas as possíveis soluções com seus respectivos fitness
    zipado.sort(key=lambda x: x[1]) # ordena as soluções pelo fitness
    return [x[0] for x in zipado[:len(populacao)//2]] # retorna as soluções com os melhores fitness

def elitismo_composto(populacao, fitness):
    '''
    faz uma seleção ordenada mei doida onde metade da população atual vai
    para a próxima geração
    serão selecionados metade da população, dessa forma:
    - 1/4 dos melhores
    - 1/4 aleatórios, podendo ser dos piores ou melhores
    sem elementos repetidos
    @param populacao: lista de individuos com o formato [objeto alocado, coordenadas]
    @param fitness: lista de valores de fitness para cada individuo
    @return: lista de individuos selecionados
    '''
    zipado = list(zip(populacao, fitness))
    zipado.sort(key=lambda x: x[1])
    melhores = [x[0] for x in zipado[:(len(populacao)//4)]] # seleciona os 1/4 melhores
    metade = len(populacao) // 2
    selecionados = set(melhores)
    while len(selecionados) < metade:
        selecionados.add(random.choice(populacao)) # seleciona aleatoriamente os outros 1/4

    return list(selecionados)