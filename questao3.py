import sys
from grafos.grafo import Grafo
from grafos.coloracao_minima import calc_lawlers_algorithm

def format_output(color_groups: list[set]) -> str:
    result = f"Coloração mínima: {len(color_groups)} cores"
    for color_index in range(len(color_groups)):
        result += f"\nVértices com número cromático {color_index + 1} - {set([vertex + 1 for vertex in color_groups[color_index]])}"
    return result

if __name__ == "__main__":
    try:
        arquivo = sys.argv[1]
    except IndexError:
        print('Entrada incorreta. Tente escrever:')
        print('>> python3 questao3.py <arquivo grafo>')
        exit()
        
    grafo = Grafo(arquivo)
    result = calc_lawlers_algorithm(grafo)
    print(format_output(result))