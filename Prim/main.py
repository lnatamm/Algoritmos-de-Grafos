import os

INFINITY = 1000000

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

#Lê a matriz de adjacência do arquivo "prim.txt"
def readFile():
    filePath = os.getcwd() + "\\Prim\\prim.txt"
    file = open(filePath)
    N = file.readline()
    N = removeLineBreak(N)
    G = []

    for i in range(N):
        G.append([])
        line = file.readline().split()
        for j in range(N):
            G[i].append(float(line[j]))

    r = file.readline()
    r = removeLineBreak(r)
    return G, r

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

def isConected(G):
    for v in dfs(G):
        #Caso haja algum vértice que não foi visitado no dfs, o grafo G é desconexo
        if(v < 2):
            return False
    return True

def hasElements(Q):
    for i in range(len(Q)):
        if(Q[i] == True):
            return True
    return False

def extractMin(Q, keys):
    minimumKey = INFINITY
    index = -1
    for i in range(len(Q)):
        if(Q[i] == True and keys[i] < minimumKey):
            minimunKey = keys[i]
            index = i
    return index

def prim(G, r):
    n = len(G)
    keys = [INFINITY]*n
    Pi = [-1]*n
    keys[r] = 0
    Q = [True]*n
    while(hasElements(Q)):
        u = extractMin(Q, keys)
        Q[u] = False
        for v in range(n):
            if(G[u][v] > 0):
                if(Q[v] == True and G[u][v] < keys[v]):
                    Pi[v] = u
                    keys[v] = G[u][v]
    return Pi

G, r = readFile()
if(isConected(G)):
    print("VERDADEIRO")
    print(prim(G, r))
else:
    print("FALSO")