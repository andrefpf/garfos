from math import inf

def busca_em_largura(grafo, vertice_inicial: int):
    vertice_inicial -= 1
    conhecido = [False] * grafo.n_vertices
    distancia = [inf] * grafo.n_vertices
    antecessor = [None] * grafo.n_vertices
    conhecido[vertice_inicial] = True
    distancia[vertice_inicial] = 0
    fila = []
    fila.append(vertice_inicial)

    while len(fila) > 0:
        u = fila.pop(0)
        vizinhos = [x-1 for x in grafo.vizinhos(u+1)]
        #index_vizinhos = [grafo.vizinhos(vizinho) for vizinho in vizinhos]
        for v in vizinhos:
            if conhecido[v] == False:
                conhecido[v] = True
                distancia[v] = distancia[u] + 1
                antecessor[v] = u
                fila.append(v)

    return (distancia, antecessor)