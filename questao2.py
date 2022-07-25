import sys
from grafos.grafo import Grafo
from grafos.hopcroft_karp import hopcroft_karp

def format_output(result):
    print(result[0])
    pairs = result[1]
    string = ""

    for i in range(len(pairs)):
        string += "({}, {}) ".format(i+1, pairs[i])

    print(string)
        

if __name__ == '__main__':
    try:
        arquivo = sys.argv[1]
        div = int(sys.argv[2])
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao3.py <arquivo grafo> <divisão>')
        exit()

    grafo = Grafo(arquivo)
    format_output(hopcroft_karp(grafo, div))