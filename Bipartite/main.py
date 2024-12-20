import os

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

#Lê a matriz de adjacência do arquivo "kruskal.txt"
def readFile():
    filePath = os.getcwd() + "\\Bipartite\\matriz.txt"
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
def DFSvisit(u, Pi, state, root, cycle, nCycles, oddCycles, parts, currentPart):
    n = len(G)
    state[u] = 1
    #Adiciona o vértice atual na parte atual (0 ou 1)
    parts[currentPart].append(u)
    #Atualiza a parte atual para a próxima, ciclando entre 0 ou 1
    currentPart = (currentPart + 1) % 2
    #Loop para cada vizinho de v
    for v in range(n):
        if(G[u][v] == 1):
            if(state[v] == 0):
                root[v] = root[u]
                Pi[v] = u
                #Atualiza os valores de todos os parametros e é feita a visitação do vértice v
                Pi, state, root, cycle, nCycles, oddCycles, parts, currentPart = DFSvisit(v, Pi, state, root, cycle, nCycles, oddCycles, parts, currentPart)
            #Caso o vértice v já tenha sido visitado, o vértice v não seja o próprio predecessor de u,
            #u e v possuem as mesmas raízes e v não é o próprio u, isso significa que o vértice v é o começo de um ciclo
            elif(state[v] == 1 and Pi[u] != v and root[v] == root[u] and u != v):
                current = u
                cycle[nCycles].append(current)
                #Enquanto o current (atual) for diferente de v (o vértice inicial do ciclo)
                while(current != v):
                    current = Pi[current]
                    cycle[nCycles].append(current)
                #Caso o ciclo seja ímpar
                if(len(cycle[nCycles]) % 2 != 0):
                    #Adiciona o ciclo nos ciclos que tornam o grafo não bipartido
                    oddCycles.append(cycle[nCycles])
                nCycles = nCycles + 1
                cycle.append([])
    state[u] = 2
    return Pi, state, root, cycle, nCycles, oddCycles, parts, currentPart

def getOddCycles(G):
    #Tamanho de G
    n = len(G)
    #Inicializa o array com os predecessores de cada vértice
    Pi = [-1]*n
    #Inicializa os estados de cada vértice. 0: Não visitado; 1: Visitado; 2: Finalizado
    state = [0]*n
    #Inicializa as raizes de cada vértice como -1
    root = [-1]*n
    #Um array que armazena todos os ciclos do grafo
    cycle = [[]]
    #Variável que indica o ciclo a ser armazenado
    nCycles = 0
    #Array que armazena todos os ciclos que tornam o grafo não bipartido
    oddCycles = []
    #Array que separa as partes do grafo em 2
    parts = [[], []]
    #Variável que indica a parte atual do vértice
    currentPart = 0
    #Loop para cada vértice u
    for u in range(n):
        if state[u] == 0:
            root[u] = u
            #Atualiza os valores de todos os atributos e é feita a visitação do vértice u
            Pi, state, root, cycle, nCycles, oddCycles, parts, currentPart = DFSvisit(u, Pi, state, root, cycle, nCycles, oddCycles, parts, currentPart)

    #Inverte a ordem dos ciclos já que armazenamos eles em ordem contrária
    for i in range(len(oddCycles)):
        oddCycles[i].reverse()
    return oddCycles, parts

def isBipartite(G):
    #Recebe os ciclos ímpares e as partes
    oddCycles, parts = getOddCycles(G)
    #Retorna se possui ciclo ímpar, os ciclos ímpares e as suas partes
    return len(oddCycles) == 0, oddCycles, parts

G = readFile()

bipartite, oddCycles, parts = isBipartite(G)
if(bipartite):
    print(f"Sim, e suas partes são: {parts[0]} e {parts[1]}")
else:
    print(f"Não, pois {oddCycles} formam ciclo ímpar")