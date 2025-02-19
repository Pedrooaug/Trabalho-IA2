import random
import math

def dist_euclidiana(x1, y1, x2, y2):
    return math.floor(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

    # Cada indivíduo é uma possível solução para o problem, compondo (I,(x,y)), onde I é o objeto (indo de A até Z e sendo gerada aleatoriamente) e (x,y) é a coordenada do local onde o objeto está alocado
def gerar_populacao(n):
    populacao = []
    #Gerando string de A até Z, para escolhermos um índice aleatório da string como objeto
    objetos = ''.join([chr(i) for i in range(65, 65 + n)])
    for _ in range(n):
        #Gerando uma solução candidata aleatória
        solucao = ''.join(random.sample(objetos, n))
        #Gerando as coordenadas para cada objeto
        coordenadas = [(random.randint(0, 30), random.randint(0, 30)) for _ in range(n)]
        populacao.append((solucao, coordenadas))
    return populacao

def gerar_matrizes(n):
    # Gera coordenadas fixas para os locais (não para os indivíduos!)
    locais = [(random.randint(0, 30), random.randint(0, 30)) for _ in range(n)]
    
    # Matriz de distância entre locais (baseada nas coordenadas)
    matriz_distancia = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                x1, y1 = locais[i]
                x2, y2 = locais[j]
                matriz_distancia[i][j] = dist_euclidiana(x1, y1, x2, y2)
    
    # Matriz de fluxo entre instalações (simétrica e diagonal zero)
    matriz_fluxo = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            fluxo = random.randint(0, 2 * n)
            matriz_fluxo[i][j] = fluxo
            matriz_fluxo[j][i] = fluxo
    
    return matriz_distancia, matriz_fluxo

def print_matriz(matriz):
    for linha in matriz:
        print(linha)

if __name__ == '__main__':
    n = 5
    matriz_distancia, matriz_fluxo = gerar_matrizes(n)
    print('Matriz de distância:')
    print_matriz(matriz_distancia)
    print('Matriz de fluxo:')
    print_matriz(matriz_fluxo)
    print('População:')
    populacao = gerar_populacao(n)
    for i, (solucao, coordenadas) in enumerate(populacao):
        print(i, solucao, coordenadas)
