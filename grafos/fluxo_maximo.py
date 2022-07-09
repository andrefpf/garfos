def edmons_karp(grafo, s, t, residuos):
    visitados = [False for _ in range(grafo.qtdVertices())]
    caminho = [None for _ in range(grafo.qtdVertices())]

    visitados[s] = True
    fila = []
    q.append(s)

    while fila:
        u = fila.pop(0)
        for v in grafo.vizinhos(u):
            if not visitados[v] and residuos.peso(u,v) > 0:
                visitados[v] = True
                caminho[v] = u

                if v == t:
                    p = [t]
                    w = t 
                    while w != s:
                        w = a[w]
                        p = [w] + p
                    return p
            fila.append(v)

    return None