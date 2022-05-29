def calc_hierholzer(grafo) -> str:

    arestas_conhecidas = dict().fromkeys(grafo.funcao_peso.keys(), False)
    vertice = 0

    (resultado, ciclo) = __subciclo_euleriano__(grafo, vertice, arestas_conhecidas)
    if resultado == False:
        return (False, None)
    else:
        if False in arestas_conhecidas.values():
            return (False, None)
        else:
            return (True, ciclo)

def __subciclo_euleriano__(grafo, vertice: int, arestas_conhecidas: dict):
    ciclo = [vertice]
    vertice_inicial = vertice
    existe_aresta_nao_visitada = False
    while True:
        existe_aresta_nao_visitada = False
        for vizinho in range(grafo.n_vertices):
            if vizinho == vertice:
                continue
            if frozenset({vizinho, vertice}) not in arestas_conhecidas.keys():
                continue
            if arestas_conhecidas[frozenset({vizinho, vertice})] == False:
                aresta = frozenset({vizinho, vertice})
                arestas_conhecidas[aresta] = True
                vertice = vizinho
                ciclo.append(vertice)
                existe_aresta_nao_visitada = True

        if not existe_aresta_nao_visitada:
            return (False, None)

        if vertice == vertice_inicial:
            break

    vertices_faltantes = []
    for vertice in ciclo:
        for aresta, conhecida in arestas_conhecidas.items():
            if vertice in aresta:
                if conhecida == False:
                    vertices_faltantes.append(aresta)

    for vertice_faltante in vertices_faltantes:
        (resultado, ciclo_) = grafo.__subciclo_euleriano__(vertice_faltante, arestas_conhecidas)
        if resultado == False:
            return (False, None)

        i = ciclo.index(vertice_faltante)
        ciclo = ciclo[:i] + ciclo_ + ciclo[i+1:]

    return (True, [x+1 for x in ciclo])