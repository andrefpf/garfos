from math import inf 


def kruskal(grafo):
    peso_aresta = lambda aresta: aresta[2]

    arestas_seguras = [] 
    arestas_ordenadas = sorted(grafo.arestas(), key=peso_aresta)
    grupos = ['odeio indexar por 1'] + [set([v+1]) for v in range(grafo.qtdVertices())]

    for u, v, w in arestas_ordenadas:
        if grupos[u] == grupos[v]:
            continue

        arestas_seguras.append((u,v,w))
        union = grupos[u].union(grupos[v])

        for i in union:
            grupos[i] = union

    return arestas_seguras