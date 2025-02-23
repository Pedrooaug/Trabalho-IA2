import random
import math

def dist_euclidiana(x1, y1, x2, y2):
    return math.floor(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

def gerar_locais(n):
    return [(random.randint(0, 30), random.randint(0, 30)) for _ in range(n)]

def gerar_instalacoes(n):
    instalacoes = [chr(i) for i in range(65, 65 + n)]  # Ex: n=3 → ['A', 'B', 'C']
    return instalacoes

# Cada indivíduo é uma possível solução para o problem, compondo (I,(x,y)), onde I é o objeto (indo de A até Z e sendo gerada aleatoriamente) e (x,y) é a coordenada do local onde o objeto está alocado
# Um exemplo de indivíduo seria ('A'(1,2)) que seria a alocação do objeto A no local (1,2)
def gerar_populacao(n, instalacoes, locais_fixos):
    populacao = []
    for _ in range(n):
        # Embaralha os locais para criar uma permutação
        locais_permutados = random.sample(locais_fixos, len(locais_fixos))
        # Combina cada instalação com um local permutado
        individuo = list(zip(instalacoes, locais_permutados))
        populacao.append(individuo)
    return populacao

def gerar_matrizes(locais_fixos, instalacoes):
    n = len(locais_fixos)
    # Matriz de distância entre locais (baseada nas coordenadas)
    matriz_distancia = [
        [dist_euclidiana(x1, y1, x2, y2) for (x2, y2) in locais_fixos]
        for (x1, y1) in locais_fixos
    ]
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
