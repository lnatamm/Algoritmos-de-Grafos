import os

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

#Lê a matriz de adjacência do arquivo "dfs.txt"
def readFile():
    filePath = os.getcwd() + "\\DFS\\dfs.txt"
    file = open(filePath)
    N = file.readline()
    N = removeLineBreak(N)
    G = []

    for i in range(N):
        G.append([])
        line = file.readline().split()
        for j in range(N):
            G[i].append(float(line[j]))

    return G

#Realiza a visita do vértice dentro do dfs
def DFSvisit(u, discovery, finalization, time, d, Pi, state, root):
    n = len(G)
    state[u] = 1
    time = time+1
    discovery[u] = time
    #Loop para cada vizinho de v
    for v in range(n):
        if(G[u][v] == 1 and state[v] == 0):
            root[v] = root[u]
            d[v] = [root[u], d[u][1] + 1]
            Pi[v] = u
            #Atualiza os valores de todos os parametros e é feita a visitação do vértice v
            discovery, finalization, time, d, Pi, state, root = DFSvisit(v, discovery, finalization, time, d, Pi, state, root)
    state[u] = 2
    time = time + 1
    finalization[u] = time
    return discovery, finalization, time, d, Pi, state, root

def DFS(G):
    #Tamanho de G
    n = len(G)
    #Inicializa os tempos de descoberta de todos os vértices
    discovery = [0]*n
    #Inicializa os tempos de finalização de todos os vértices
    finalization = [0]*n
    #Define o tempo atual (inicial) como 0
    time = 0
    #Inicializa o array com as distâncias de cada vértice para cada raiz
    d = [[-1, 0]]*n
    #Inicializa o array com os predecessores de cada vértice
    Pi = [-1]*n
    #Inicializa os estados de cada vértice. 0: Não visitado; 1: Visitado; 2: Finalizado
    state = [0]*n
    #Inicializa as raizes de cada vértice como -1
    root = [-1]*n
    
    #Loop para cada vértice u
    for u in range(n):
        if state[u] == 0:
            root[u] = u
            d[u] = [root[u], 0]
            #Atualiza os valores de todos os atributos e é feita a visitação do vértice u
            discovery, finalization, time, d, Pi, state, root = DFSvisit(u, discovery, finalization, time, d, Pi, state, root)

    return discovery, finalization, d, Pi, state, root

G = readFile()
discovery, finalization, d, Pi, state, root = DFS(G)
print("Discovery:")
print(discovery)
print("Finalization:")
print(finalization)
print("Pi")
print(Pi)
print("D:")
print(d)
print("States:")
print(state)
print("Roots:")
print(root)