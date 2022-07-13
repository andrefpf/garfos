import sys
from grafos.grafo import Grafo
from grafos.tarjan import tarjan_scc

if __name__ == '__main__':
    try:
        grafo = Grafo(sys.argv[1])
        tarjan_scc(grafo)
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao1.py <arquivo grafo>')
        exit()