import sys
from grafos.grafo import Grafo
from grafos.fluxo_maximo import edmons_karp
from math import inf


def max_flux(grafo, fluxo):
    maxf = inf 
    for inicio, fim in zip(fluxo, fluxo[1:]):
        w = grafo.peso(inicio, fim)
        if w < maxf:
            maxf = w    
    return maxf

if __name__ == '__main__':
    try:
        arquivo = sys.argv[1]
        origem = int(sys.argv[2])        
        destino = int(sys.argv[3])        
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao3.py <arquivo grafo> <origem> <destino>')
        exit()
        
    grafo = Grafo(arquivo)
    fluxo = edmons_karp(grafo, origem, destino, None)
    maxf = max_flux(grafo, fluxo)
    print(maxf)