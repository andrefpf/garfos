from math import inf

class Grafo:
    def __init__(self, caminho_do_arquivo="", ler_arquivo=True, vertices=set(), edges={}):
        self.grafo = []
        self.rotulos = []
        self.n_vertices = 0
        self.n_arestas = 0
        self.funcao_peso = {}
        self.directed = False
        self.lista_vertices = set()
        if ler_arquivo:
            self.ler(caminho_do_arquivo)
        else:
            self.n_vertices = len(vertices)
            self.n_arestas = len(edges)
            self.lista_vertices = vertices
            self.funcao_peso = edges

    def getVertices(self):
        return self.lista_vertices

    def qtdVertices(self):
        return self.n_vertices

    def qtdArestas(self):
        return self.n_arestas

    def grau(self, v):
        degree = 0
        if v-1 < len(self.grafo):
            for value in self.grafo[v-1]:
                if value != inf:
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
                if value != inf:
                    lista_vizinhos.append(n+1)
                    # lista_vizinhos.append(self.rotulo(n+1))

        return lista_vizinhos

    def vizinhos_saintes(self, v):
        lista_vizinhos = []
        vertice = v - 1
        if self.directed == False:
            return self.vizinhos(v)
        for aresta in self.funcao_peso.keys():
            if aresta[0] == vertice:
                lista_vizinhos.append(aresta[1]+1)
        return lista_vizinhos

    def haAresta(self, u, v):
        if u-1 < len(self.grafo) and v-1 < len(self.grafo):
            return self.grafo[u-1][v-1] != inf
        return False

    def peso(self, u, v):
        if u-1 < len(self.grafo) and v-1 < len(self.grafo):
            return self.grafo[u-1][v-1]
        return inf

    def arestas(self):
        arestas_validas = []
        for u in range(self.qtdVertices()):
            for v in range(self.qtdVertices()):
                if self.haAresta(u+1, v+1):
                    aresta = (u+1, v+1, self.peso(u+1, v+1))
                    arestas_validas.append(aresta)
        return arestas_validas
        
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

            if "*arcs" in linha:
                flag = False
                self.directed = True
                continue

            if flag:
                vertice, rotulo = linha.split(" ", 1)
                vertice = float(vertice)
                self.lista_vertices.add(len(self.lista_vertices))
                self.rotulos.append(rotulo)

                self.grafo[int(vertice)-1] = self.n_vertices*[inf]
            else:
                u, v, valor = [float(i) for i in linha.split()]
                u, v = int(u), int(v) #deixar isso por enquanto pra garantir que não
                                      #seja passado indice zoado, arrumo depois

                if u-1 < len(self.grafo) and v-1 < len(self.grafo):
                    self.grafo[u-1][v-1] = valor
                    if (self.directed):
                        aresta = (u-1, v-1)
                        self.funcao_peso[aresta] = valor
                    else:
                        self.grafo[v-1][u-1] = valor
                        aresta = frozenset({u-1,v-1})
                        self.funcao_peso[aresta] = valor
                        
                self.n_arestas += 1