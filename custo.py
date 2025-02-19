def custo (obj, loc, funcPeso, funcDist):
    '''
        Função a ser minimizada na aplicação dos algoritmos genéticos
        @param obj: lista de tamanho n de objetos que vao ser alocados
        @param loc: lista de tamanho n de locais onde os objetos vao ser alocados
        @param funcPeso: função que retorna o peso de um objeto
    '''
    custo = 0
    for i,j in range obj:
        custo += funcPeso(obj[i], obj[j]) * funcDist(loc[i], loc[j])