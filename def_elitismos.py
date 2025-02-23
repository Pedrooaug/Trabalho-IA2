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
    zipado.sort(key=lambda x: x[1]) # ordena as soluções pelo fitness em ordem decrescente
    #print(zipado[0][0])
    selecionados = zipado[:len(populacao)//2] # seleciona as soluções com os melhores fitness
    return [x[0] for x in selecionados]

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
    melhores = zipado[:len(populacao)//4] # seleciona os 1/4 melhores
    metade = len(populacao) // 2
    while len(melhores) < metade:
         #seleciona aleatoriamente os outros 1/4
        i = random.randint(0, len(populacao)-1)
        if populacao[i] not in melhores:
            melhores.append(populacao[i])


    return melhores
