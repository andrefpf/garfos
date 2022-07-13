import sys
from grafos.grafo import Grafo
from grafos.ordenacao_topologica import ordenacao_topologica
from typing import Type

def format_output(grafo: Type[Grafo], ordenacao_topologica: list) -> str:
    output = ""
    for vertice in ordenacao_topologica:
        output += f"{grafo.rotulo(vertice)} → "
    return output[:-3]+"."

if __name__ == '__main__':
    try:
        arquivo = sys.argv[1]
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao2.py <arquivo grafo>')
        exit()
        
    grafo = Grafo(arquivo)
    resultado = ordenacao_topologica(grafo)
    print(format_output(grafo, resultado))