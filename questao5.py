import sys
from grafos.grafo import Grafo
from grafos.floyd_warshall import floyd_warshall

def format_output(distancias):
    for i in range(len(distancias)):
        paths = ','.join([str(x) for x in distancias[i]])
        print("{}:{}".format(i+1, paths))

        # Caso seja necessario um espacamento entre os dois pontos
        # e as distâncias
        #print("{}: {}".format(i+1, paths))

def calc_floyd_warshall(arquivo):
    grafo = Grafo(arquivo)

    distancias = floyd_warshall(grafo)
    format_output(distancias)

if __name__ == '__main__':
    try:
        arquivo = sys.argv[1]
        calc_floyd_warshall(arquivo)
    except FileNotFoundError:
        print('Arquivo inexistente. Tente escrever:')
        print('>> python3 questao5.py <arquivo grafo>')
    except:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao5.py <arquivo grafo>')