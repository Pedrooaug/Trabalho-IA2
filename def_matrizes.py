'''
Uma matriz d de distâncias entre cada par de locais x, y ∈ {0, 1, 2, . . . , n − 1}.
Para gerar uma entrada aleatória de tamanho n, você deve gerar n pares de coordenadas
aleatórias e calcular a Distância Euclidiana entre esses pontos. Para simplificar mais
as coisas, recomendo usar o piso da distância euclidiana, pois isso garantirá valores
inteiros. Recomendo também limitar os valores das coordenadas ao grid que usamos
no primeiro trabalho com valores inteiros no intervalo [0, 30]. Isso permitirá que você
reutilize partes do código do primeiro trabalho para obter a matriz de distâncias.
'''

'''
Uma matriz f de fluxo entre cada par de instalações x, y ∈ {0, 1, 2, . . . , n − 1}.
Para obter uma matriz de fluxo, basta preencher a matriz aleatoriamente com números
inteiros aleatórios, preservando a simetria e a diagonal principal nula. Sugiro manter
esses valores entre os inteiros do conjunto {0, 1, 2, 3, . . . , 2n − 1, 2n}.
'''

import random
import math

def dist_euclidiana(x1, y1, x2, y2):
    return math.floor(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

#Os elementos da matriz de distância será no formato ((x1,y1)(x2,y2),euc) onde x1 e y1 formam o primeiro para de coordenadas, x2 e y2 o segundo para de coordenadas e euc é a distância euclidiana entre os pares
#A matriz de fluxo é simética e a diagonal principal é nula, e seus elementos são no formato ((x,y),fluxo) onde x e y são as coordenadas e fluxo é o valor entre 0 e 2n
#As duas matrizes devem ser preenchidas em conjunto, para garantir que os valores de cada par de coordenadas sejam iguais, preservando a aleatoriedade gerada

def gerar_matrizes(n):
    matriz_distancia = []
    matriz_fluxo = []
    for i in range(n):
        linha_distancia = []
        linha_fluxo = []
        for j in range(n):
            if i == j:
                linha_distancia.append(((i,i),(0)))
                linha_fluxo.append(((i,i),(0)))
            elif j < i:
                linha_distancia.append(matriz_distancia[j][i])
                linha_fluxo.append(matriz_fluxo[j][i])
            else:
                x1 = random.randint(0,30)
                y1 = random.randint(0,30)
                x2 = random.randint(0,30)
                y2 = random.randint(0,30)
                euc = dist_euclidiana(x1,y1,x2,y2)
                fluxo = random.randint(0,2*n)
                linha_distancia.append(((x1,y1),(x2,y2),euc))
                linha_fluxo.append(((x1,y1),(x2,y2),fluxo))
        matriz_distancia.append(linha_distancia)
        matriz_fluxo.append(linha_fluxo)
    return matriz_distancia, matriz_fluxo

def print_matriz(matriz):
    for linha in matriz:
        print(linha)

if __name__ == '__main__':
    n = 5
    print('Matriz de distâncias:')
    print_matriz(gerar_matrizes(n)[0])
    print('Matriz de fluxo:')
    print_matriz(gerar_matrizes(n)[1])

