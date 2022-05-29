def calc_floyd_warshall(grafo):
    size = grafo.qtdVertices()
    D = [[float('inf') for _ in range(size)] for _ in range(size)]

    for u in range(size):
        for v in range(size):
            if u == v:
                D[u][v] = 0
            else:
                D[u][v] = grafo.peso(u+1, v+1)

    for k in range(size):
        D_prev = D.copy()
        for u in range(size):
            for v in range(size):
                D[u][v] = min(D_prev[u][v], D_prev[u][k] + D_prev[k][v])

    return D

def floyd_warshall(grafo):
    min_path = calc_floyd_warshall(grafo)
    for i in range(len(min_path)):
        paths = ','.join([str(x) for x in min_path[i]])
        print("{}:{}".format(i+1, paths))