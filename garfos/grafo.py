class Grafo:
    def __init__(self, caminho_do_arquivo):
        self.grafo = []
        self.rotulos = []
        self.n_vertices = 0
        self.n_arestas = 0
        self.funcao_peso = {}

        self.ler(caminho_do_arquivo)

    def qtdVertices(self):
        return self.n_vertices

    def qtdArestas(self):
        return self.n_arestas

    def grau(self, v):
        degree = 0
        if v-1 < len(self.grafo):
            for value in self.grafo[v-1]:
                if value != float('inf'):
                    degree += 1
        
        return degree

    def rotulo(self, v):
        name = "Vértice não percente ao grafo."

        if v-1 < len(self.grafo):
            name = self.rotulos[v-1]

        return name
    
    def vizinhos(self, v):
        lista_vizinhos = []

        if v-1 < len(self.grafo):
            for n, value in enumerate(self.grafo[v-1]):
                if value != float('inf'):
                    lista_vizinhos.append(self.rotulo(n+1))

        return lista_vizinhos

    def haAresta(self, u, v):
        if u-1 < len(self.grafo) and v-1 < len(self.grafo):
            return self.grafo[u-1][v-1] != float('inf')
        
        return False

    def peso(self, u, v):
        if u-1 < len(self.grafo) and v-1 < len(self.grafo):
            return self.grafo[u-1][v-1]
        
        return float('inf')

    def ler(self, caminho_do_arquivo):
        arquivo = open(caminho_do_arquivo)
        linhas = arquivo.read().splitlines()
        flag = False
        
        for linha in linhas:
            if "*vertices" in linha:
                self.n_vertices = int(linha.split(" ")[1])
                self.grafo = self.n_vertices*[[]]
                flag = True
                continue

            if "*edges" in linha:
                flag = False
                continue

            if flag:
                vertice, rotulo = linha.split(" ")
                vertice = int(vertice)

                self.rotulos.append(rotulo)

                self.grafo[vertice-1] = self.n_vertices*[float('inf')]
            else:
                u, v, valor = [int(i) for i in linha.split(" ")]

                if u-1 < len(self.grafo) and v-1 < len(self.grafo):
                    self.grafo[u-1][v-1] = valor
                    self.grafo[v-1][u-1] = valor
                    aresta = frozenset({u-1,v-1})
                    self.funcao_peso[aresta] = valor

                self.n_arestas += 1

    def ciclo_euleriano(self) -> (bool, list):
        arestas_conhecidas = dict().fromkeys(self.funcao_peso.keys(), False)
        vertice = 0
        (resultado, ciclo) = self.__subciclo_euleriano__(vertice, arestas_conhecidas)
        if resultado == False:
            return (False, None)
        else:
            if False in arestas_conhecidas.values():
                return (False, None)
            else:
                return (True, ciclo)

    def __subciclo_euleriano__(self ,vertice: int, arestas_conhecidas: dict) -> (bool, list):
        ciclo = [vertice]
        vertice_inicial = vertice
        existe_aresta_nao_visitada = False
        while True:
            existe_aresta_nao_visitada = False
            for vizinho in range(self.n_vertices):
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
                        arestas_faltantes.append(aresta)

        for vertice_faltante in vertices_faltantes:
            (resultado, ciclo_) = self.__subciclo_euleriano__(vertice_faltante, arestas_conhecidas)
            if resultado == False:
                return (False, None)

            i = ciclo.index(vertice_faltante)
            ciclo = ciclo[:i] + ciclo_ + ciclo[i+1:]

        return (True, [x+1 for x in ciclo])


teste = Grafo("w.txt")
print("qtd", teste.qtdVertices(), teste.qtdArestas())
print("grau", teste.grau(5), teste.grau(3), teste.grau(1), teste.grau(2))
print("rotulo", teste.rotulo(1), teste.rotulo(3), teste.rotulo(5))
print("vizinhos", teste.vizinhos(1), teste.vizinhos(3), teste.vizinhos(5), teste.vizinhos(2))
print("haaresta", teste.haAresta(1, 3), teste.haAresta(3, 1), teste.haAresta(1, 2), teste.haAresta(2, 1))
print("peso", teste.peso(1, 3), teste.peso(3, 1), teste.peso(3, 5), teste.peso(1, 2))
print("lista adjacencias", teste.funcao_peso)
print(teste.ciclo_euleriano())

#*vertices n
# 1 rotulo_1
# 2 rotulo_2
# 3 rotulo_3
#*edges
# a b valor_peso
# a c valor_peso
# 
