def floyd_warshall(grafo):
    size = grafo.qtdVertices()
    distancias = [[float('inf') for _ in range(size)] for _ in range(size)]

    for u in range(size):
        for v in range(size):
            if u == v:
                distancias[u][v] = 0
            else:
                distancias[u][v] = grafo.peso(u+1, v+1)

    for k in range(size):
        for u in range(size):
            for v in range(size):
                distancias[u][v] = min(distancias[u][v], distancias[u][k] + distancias[k][v])

    return distancias