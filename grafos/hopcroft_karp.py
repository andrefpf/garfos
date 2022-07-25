from math import inf

g = 0
u, v = 0, 0
pair_u, pair_v, dist = [], [], []
NIL = 0

def hopcroft_karp(grafo, div):
    global g, u, v 
    global pair_u, pair_v, dist

    g = grafo
    u = div
    v = grafo.qtdVertices() - u

    pair_u = [0] * (u+1)
    pair_v = [0] * (v+1)
    dist = [-1]* (u+1)

    matching = 0

    while (bfs()):
        for i in range(1, u+1):
            if pair_u[i] == 0 and dfs(i):
                matching += 1

    return (matching, pair_u)

def bfs():
    global g, u, v 
    global pair_u, pair_v, dist

    queue = []

    for i in range(1, u+1):
        if pair_u[i] == 0:
            dist[i] = 0
            queue.append(i)
        else:
            dist[i] = inf

    dist[0] = inf

    while (len(queue) > 0):
        k = queue.pop(0)
        if dist[k] < dist[0]:
            for j in g.vizinhos(k):
                if dist[pair_v[j-u]] == inf:
                    dist[pair_v[j-u]] = dist[k] + 1
                    queue.append(pair_v[j-u])

    return dist[0] != inf


def dfs(i):
    global g, u, v 
    global pair_u, pair_v, dist

    if i != 0:
        for j in g.vizinhos(i):
            if dist[pair_v[j-u]] == dist[i] + 1:
                if dfs(pair_v[j-u]):
                    pair_v[j-u] = i
                    pair_u[i] = j
                    return True

        dist[i] = inf
        return False

    return True