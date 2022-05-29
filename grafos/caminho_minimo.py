from math import inf 


class MinHeap:
    def __init__(self, sequence):
        self.data = sequence
        self.indexes = sorted(list(range(len(sequence))))

    def __setitem__(self, key, val):
        self.set_by_index(key, val)

    def __getitem__(self, key):
        return self.get_by_index(key)

    def empty(self):
        return len(self.indexes) == 0

    def get_by_index(self, index):
        return self.data[index]

    def set_by_index(self, index, val):
        self.data[index] = val
        self.indexes.sort(key=self.get_by_index)
    
    def pop_min(self):
        return self.indexes.pop(0)


def dijkstra(grafo, origem):
    # index all by 0
    origem -= 1
    vizinhos = lambda x: [i-1 for i in grafo.vizinhos(x+1)]
    peso = lambda u, v: grafo.peso(u+1, v+1)

    caminhos = [None for _ in range(grafo.qtdVertices())]
    distancias = MinHeap([inf for _ in range(grafo.qtdVertices())])

    distancias[origem] = 0
    while not distancias.empty():
        u = distancias.pop_min()

        for v in vizinhos(u):
            if v not in distancias.indexes:
                continue

            if distancias[v] > distancias[u] + peso(u, v):
                distancias[v] = distancias[u] + peso(u, v)
                caminhos[v] = u

    # reindex to 1
    caminhos = [(i if i is None else i+1) for i in caminhos]
    return distancias, caminhos
