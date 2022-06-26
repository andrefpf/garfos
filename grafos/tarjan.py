from math import inf

n = 0
id = 0

ids = []
low = []
onStack = []
stack = []

def tarjan_scc(grafo):
    global n, id
    global ids, low, onStack, stack

    n = grafo.qtdVertices()
    id = 0

    ids = n*[inf]
    low = n*[0]
    onStack = n*[False]
    stack = []

    for i in range(0, n):
        if(ids[i] == inf):
            tarjan_dfs(i, grafo)

    format_output(low, grafo)

def tarjan_dfs(at, grafo):
    global n, id
    global ids, low, onStack, stack

    stack.append(at)
    onStack[at] = True
    ids[at], low[at] = id, id
    id += 1

    vizinhos = [v-1 for v in grafo.vizinhos_saintes(at+1)]

    for v in vizinhos:
        if ids[v] == inf:
            tarjan_dfs(v, grafo)
        if(onStack[v]):
            low[at] = min(low[at], low[v])

    if(ids[at] == low[at]):
        for _ in range(len(stack)):
            node = stack.pop()
            low[node] = ids[at]
            if (node == at):
                break

def format_output(scc, grafo):
    ids = list(dict.fromkeys(scc))
    for id in ids:
        if scc.count(id) > 1:
            vertices_scc = [i for i in range(0, len(scc)) if scc[i] == id]
            for v in vertices_scc:
                if any(v in vertices_scc for v in grafo.vizinhos_saintes(v)):
                    print(",".join([str(v+1) for v in vertices_scc]))
        elif id+1 in grafo.vizinhos_saintes(id+1):
            print(id+1)