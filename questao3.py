import sys
from garfos.grafo import Grafo
from garfos.ciclo_euleriano import calc_hierholzer

def format_output(existe_ciclo: bool, ciclo: list):
    if not existe_ciclo:
            return "0"
    else:
        ciclo_string = [str(vertice) for vertice in ciclo]
        return "1\n" + ",".join(ciclo_string)

if __name__ == '__main__':
    try:
        arquivo = sys.argv[1]
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao3.py <arquivo grafo>')
    grafo = Grafo(arquivo)
    (resultado, ciclo) = calc_hierholzer(grafo)
    print(format_output(resultado, ciclo))