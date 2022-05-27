from math import inf 


def dijkstra(grafo, origem):
    # index all by 0
    origem -= 1
    vizinhos = lambda x: [i-1 for i in grafo.vizinhos(x+1)]
    peso = lambda u, v: grafo.peso(u+1, v+1)

    caminhos = [None for _ in range(grafo.qtdVertices())]
    visitados = [False for _ in range(grafo.qtdVertices())]
    distancias = [inf for _ in range(grafo.qtdVertices())]

    distancias[origem] = 0
    while not all(visitados):
        tmp = inf
        u = inf
        for i, val in enumerate(distancias):
            if (val <= tmp) and not visitados[i]:
                u = i 
                tmp = val
        visitados[u] = True


        for v in vizinhos(u):
            if distancias[v] > distancias[u] + peso(u, v):
                distancias[v] = distancias[u] + peso(u, v)
                caminhos[v] = u

    # reindex to 1
    caminhos = [(i if i is None else i+1) for i in caminhos]
    return distancias, caminhos
