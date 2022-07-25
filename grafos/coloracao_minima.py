from math import inf
from typing import List, Type
from grafos.grafo import Grafo
import itertools

def calc_lawlers_algorithm(grafo: Type[Grafo]) -> list[set]:
    color_groups = []

    vertices = list(range(grafo.qtdVertices()))
    powerset = get_powerset(vertices)

    subset_keys = [frozenset(x) for x in powerset]
    colors = [None] * (len(powerset))
    colors_per_subset = dict(zip(subset_keys, colors)) 
    colors_per_subset[frozenset()] = 0

    for subset in powerset[1:]:
        colors_per_subset[frozenset(subset)] = inf

        subgraph_edges = get_edges_belonging_to_subset(subset, grafo)
        subgraph = Grafo(ler_arquivo=False, vertices=subset, edges=subgraph_edges)

        maximal_independent_sets = list_all_maximal_independent_sets(subgraph)
        if subset == powerset[-1]:
            color_groups = maximal_independent_sets

        for item in maximal_independent_sets:
            subgraph_complement = subset.difference(item)
            if colors_per_subset[frozenset(subgraph_complement)] + 1 < colors_per_subset[frozenset(subset)]:
                colors_per_subset[frozenset(subset)] = colors_per_subset[frozenset(subgraph_complement)] + 1

    return color_groups

def get_powerset(linear_collection) -> list[set]:
    powerset = []
    for subset_size in range(len(linear_collection)+1):
        for subset in itertools.combinations(linear_collection, subset_size):
            powerset.append(set(subset))
    return powerset

def get_edges_belonging_to_subset(subset: list, graph: Type[Grafo]) -> dict[frozenset, int]:
    edges = {}
    for edge, weight in graph.funcao_peso.items():
        edge = list(edge)
        if edge[0] in subset and edge[1] in subset:
            edges[frozenset(edge)] = weight
    return edges

def list_all_maximal_independent_sets(graph: Type[Grafo]) -> list[set]:
    maximal_independent_sets = list()
    vertices = graph.getVertices()
    graph_powerset = get_powerset(vertices)
    graph_powerset.reverse()

    index = 0
    limit = len(graph_powerset)
    subsets = graph_powerset
    while True:
        if index == limit:
            break
        subset = subsets[index]
        if subset in graph_powerset:
            is_maximal_independent = True
            for vertex_v in subset:
                for vertex_u in subset:
                    if frozenset([vertex_v, vertex_u]) in graph.funcao_peso.keys():
                        is_maximal_independent = False
                        break
                if not is_maximal_independent:
                    break

            if is_maximal_independent:
                subset_powerset = get_powerset(subset)
                vertices = [vertex for vertex in vertices if vertex not in subset]
                graph_powerset = get_powerset(vertices)[1:]
                graph_powerset.reverse()
                maximal_independent_sets.append(subset)
        index += 1
    return maximal_independent_sets