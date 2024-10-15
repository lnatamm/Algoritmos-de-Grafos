import os

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

#Lê a matriz de adjacência do arquivo "kruskal.txt"
def readFile():
    filePath = os.getcwd() + "\\kruskal.txt"
    file = open(filePath)
    N = file.readline()
    N = removeLineBreak(N)
    G = []

    for i in range(N):
        G.append([])
        line = file.readline().split()
        for j in range(N):
            G[i].append(int(line[j]))

    return G

#Realiza a visita do vértice dentro do dfs
def dfsVisit(v, state, Pi, timeDiscovery, timeFinalization, time):
    #Altera o estado do vértice v para visitado
    state[v] = 1
    #Incrementa o tempo atual
    time = time + 1
    #Define o tempo de descoberta do vértice v como o tempo atual
    timeDiscovery[v] = time
    #Loop para cada vizinho de v
    for i in range(len(G[v])):
        if(G[v][i] > 0):
            #Se o vértice ainda não foi visitado
            if(state[i] == 0):
                #Altera o predescessor do vértice para v
                Pi[i] = v
                #Agora visitamos o vértice i
                dfsVisit(i, state, Pi, timeDiscovery, timeFinalization, time)
    #Após todos os vizinhos de v terem sido visitados, finalizamos o vértice v
    state[v] = 2
    time = time + 1
    #Define o tempo de finalização do vértice v como o tempo atual
    timeFinalization[v] = time

#Realiza a busca em profundidade do vértice G e retorna os estados dos vértices
def dfs(G):
    n = len(G)
    #Array que indica o estado de cada vértice. 0: Não visitado; 1: Visitado; 2: Finalizado
    state = [0]*n
    #Array que indica os predecessores de cada vértice
    Pi = [-1]*n
    #Array que indica os tempos de descoberta de cada vértice
    timeDiscovery = [0]*n
    #Array que indica os tempos de finalização de cada vértice
    timeFinalization = [0]*n
    #Tempo atual da execução
    time = 0
    #Loop para todos os vértices do grafo G
    for v in range(n):
        #Se o vértice ainda não foi visitado, realizamos a visita dele
        if(state[v] == 0):
            dfsVisit(v, state, Pi, timeDiscovery, timeFinalization, time)
    #Retornamos apenas o estado de cada vértice porque só estamos realizando o dfs para verificar se
    #o grafo G é conexo ou desconexo
    return state

#Verifica se o Grafo G é conexo ou desconexo
def isConected(G):
    for v in dfs(G):
        #Caso haja algum vértice que não foi visitado no dfs, o grafo G é desconexo
        if(v < 2):
            return False
    return True

#Retorna as arestas da árvore geradora mínima do grafo G
def kruskal(G):
    n = len(G)
    # Make-Set: Cada vértice compõe a sua própria árvore. Isso significa que ele é sua própria raiz
    roots = [i for i in range(n)]

    #Retorna a raiz do vértice u
    def find_set(u):
        return roots[u]

    #Adiciona o vértice v na árvore a qual o vértice u pertence
    def union(u, v):
        #Guarda a raiz onde o vértice v será adicionado
        root = roots[u]
        #Guarda a raiz do vértice v
        oldRoot = roots[v]
        for i in range(n):
            #Altera a raiz do vértice v para a raiz do vértice u
            if(roots[i] == roots[oldRoot]):
                roots[i] = root

    minimumSpanningTree = []
    #Inicializa as arestas
    edges = []
    for i in range(n):
        for j in range(n):
            if((i > j) and (G[i][j] > 0)):
                edges.append([i, j, G[i][j]])
    #Bubble sort pelo peso das arestas
    for i in range(len(edges)):
        for j in range((len(edges) - 1)):
            if(edges[j][2] > edges[j+1][2]):
                edges[j], edges[j+1] = edges[j+1], edges[j]
    #Loop para cada aresta, ordenada em ordem crescente
    for i in range(len(edges)):
        #Se a aresta ainda não pertence à árvore, ou seja, os vértices da aresta não possuem a mesma raiz
        if(find_set(edges[i][0]) != find_set(edges[i][1])):
            #Adiciona essa aresta na lista de arestas da árvore geradora mínima
            minimumSpanningTree.append(edges[i])
            union(edges[i][0], edges[i][1])

    return minimumSpanningTree

G = readFile()
if(isConected(G)):
    print("VERDADEIRO")
    print(kruskal(G))
else:
    print("FALSO")