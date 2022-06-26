import sys
from grafos.grafo import Grafo
from grafos.arvores_geradoras_minimas import kruskal


def gerar_arvore(arquivo):
    g = Grafo(arquivo)
    arestas = kruskal(g)

    total = 0
    tmp_arestas = []
    for u,v,w in arestas:
        total += w 
        tmp_arestas.append(f'{u}-{v}')
    output_arestas = ', '.join(tmp_arestas)
    
    print(total)
    print(output_arestas)

if __name__ == '__main__':   
    try:
        arquivo = sys.argv[1]    
        gerar_arvore(arquivo)
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao5.py <arquivo grafo>')
        exit()
