import sys
from grafos.grafo import Grafo
from grafos.busca_em_largura import busca_em_largura

def extrair_niveis(distancias: list):
    distancias = [x for x in distancias if type(x) == int]
    niveis = []
    for valor in range(max(distancias) + 1):
        vertices_do_nivel = [vertice+1 for vertice, distancia in enumerate(distancias) if distancia == valor]
        niveis.append(vertices_do_nivel)
    return niveis

def format_output(niveis: list):
    output = ""
    for i in range(len(niveis)):
        nivel_string = [str(vertice) for vertice in niveis[i]]
        output += f'{i}: {",".join(nivel_string)}\n'
    return output[:-1]

if __name__ == '__main__':
    try:
        arquivo = sys.argv[1]
        vertice = int(sys.argv[2])
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao2.py <arquivo grafo> <vertice>')
        exit()

    grafo = Grafo(arquivo)
    (distancia, antecessor) = busca_em_largura(grafo, vertice)
    print(format_output(extrair_niveis(distancia)))