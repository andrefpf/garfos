from math import inf
from typing import Type
from grafos.grafo import Grafo

def ordenacao_topologica(grafo: Type[Grafo]) -> list:
    vertices = grafo.qtdVertices()
    if grafo.directed == False:
        return []
    conhecido = [False for _ in range(vertices)]
    tempo_inicio_visita = [inf for _ in range(vertices)]
    tempo_final_visita = [inf for _ in range(vertices)]
    tempo = 0
    ordenacao = []
    for vertice in range(vertices):
        if conhecido[vertice] == False:
            tempo = __DFS_visit_OT__(grafo, vertice, conhecido, tempo_inicio_visita, tempo_final_visita, tempo, ordenacao)
    return ordenacao
    
def __DFS_visit_OT__(grafo: Type[Grafo], vertice: int, conhecido: list, tempo_inicio_visita: list, 
    tempo_final_visita: list, tempo: int, ordenacao: list):
    conhecido[vertice] = True
    tempo += 1
    tempo_inicio_visita[vertice] = tempo
    for vizinho in grafo.vizinhos_saintes(vertice+1):
        vizinho = vizinho -1
        if conhecido[vizinho] == False:
            tempo = __DFS_visit_OT__(grafo, vizinho, conhecido, tempo_inicio_visita, tempo_final_visita, tempo, ordenacao)
    tempo +=1
    tempo_final_visita[vertice] = tempo
    ordenacao.insert(0, vertice+1)

    # tipos primitivos são imutáveis, logo a passagem por referência do tempo não funciona
    return tempo
