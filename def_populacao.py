'''
A população do algortimo serão n pontos gerados num intervalo de 0 a 30
'''
import random

def gerar_populacao(n):
    populacao = []
    for i in range(n):
        x = random.randint(0,30)
        y = random.randint(0,30)
        populacao.append((x,y))
    return populacao