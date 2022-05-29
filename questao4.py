import sys
from garfos.grafo import Grafo
from garfos.caminho_minimo import dijkstra


def format_output(vertice, caminho, distancia):
    str_caminho = ''.join(f'{i},' for i in caminho[:-1])
    str_caminho += f'{caminho[-1]};'
    return f'{vertice}: {str_caminho} d={distancia}'

def caminho_para_nos(arquivo, vertice):
    g = Grafo(arquivo)
    d, a = dijkstra(g, vertice)

    for v in range(g.qtdVertices()):
        v += 1

        caminho = []
        i = v
        while i is not None:
            caminho.append(i)
            i = a[i-1]

        caminho = list(reversed(caminho))
        distancia = d[v-1]

        out = format_output(vertice, caminho, distancia)
        print(out)


if __name__ == '__main__':   
    try:
        arquivo = sys.argv[1]
        vertice = int(sys.argv[2])        
        caminho_para_nos(arquivo, vertice)
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao5.py <arquivo grafo> <vertice>')