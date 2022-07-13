def edmons_karp(grafo, s, t, residuos):
    visitados = ['Index 0'] + [False for _ in range(grafo.qtdVertices())]
    caminho = ['Index 0'] + [None for _ in range(grafo.qtdVertices())]

    visitados[s] = True
    fila = []
    fila.append(s)

    while fila:
        u = fila.pop(0)
        for v in grafo.vizinhos(u):
            if not visitados[v]:
                visitados[v] = True
                caminho[v] = u

                if v == t:
                    p = [t]
                    w = t 
                    while w != s:
                        w = caminho[w]
                        p.insert(0, w)
                    return p
            fila.append(v)

    return None