INFINITY = 999999

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

#Lê a matriz de capacidade do arquivo "ff.txt"
def readFile():
    filePath = os.getcwd() + "\\Ford-Fulkerson\\ff.txt"
    file = open(filePath)
    N = file.readline()
    N = removeLineBreak(N)
    C = []

    for i in range(N):
        C.append([])
        line = file.readline().split()
        for j in range(N):
            C[i].append(float(line[j]))

    st = file.readline().split()
    s = st[0]
    t = st[1]
    return C, s, t

#Retorna o array das distâncias de cada vértice e a lista de predecessores de cada vértice de G partindo de r
def bfs(G, r):
    n = len(G)
    #Array que indica o estado de cada vértice. 0: Não visitado 1: Visitado 2: Finalizado
    state = [0]*n
    #Array que indica os predecessores de cada vértice
    Pi = [-1]*n
    #Array que indica a distância de cada vértice para a raiz r
    d = [INFINITY]*n
    state[r] = 1
    d[r] = 0
    Pi[r] = -1
    queue = []
    #Primeiro vértice a ser observado será a raiz
    queue.append(r)
    #Até todos os vértices serem visitados
    while queue != []:
        #Armazena a o vértice da posição inicial da fila
        u = queue.pop()
        for v in range(n):
            if(G[u][v] != 0 and state[v] == 0):
                state[v] = 1
                Pi[v] = u
                d[v] = 1 + d[u]
                #Adiciona o vértice v para ser visitado depois
                queue.append(v)
        state[u] = 2
    return Pi

#Encontra e retorna um caminho do vértice u pra v
def FindPath(G, u, v):
    #Armazena a lista de predecessores após a aplicação do bfs
    Pi = bfs(G, u)
    #Se o predecessor do vértice v for -1, isso significa que não existe um caminho
    if(Pi[v] == -1):
        return False, None
    #Inicializamos um vetor de caminho com o próprio v
    path = [v]
    curr = Pi[v]
    
    #O loop vai no pior dos casos percorrer toda a lista de predecessores
    for i in range(len(Pi)):
        path.append(curr)
        #Se chegamos no vértice u, já temos o caminho
        if(curr == u):
            path.reverse()
            return True, path
        #Fazemos o caminho de trás pra frente até chegar no u
        curr = Pi[curr]
    return False, None

#Função para printar a matriz de maneira bem formatada
def PrintMatrix(M):
    n = len(M)
    for i in range(n):
        if(M[i][0] >= 0):
            print(f"[ {M[i][0]}", end=",")
        else:
            print(f"[{M[i][0]}", end=",")
        for j in range(1, n-1):
            if(M[i][j] >= 0):
                print(f" {M[i][j]},", end="")
            else:
                print(f"{M[i][j]},", end="")
        if(M[i][n-1] >= 0):
            print(f" {M[i][n-1]}]")
        else:
            print(f"{M[i][n-1]}]")

#Calcula o grafo residual
def ResidualNetwork(C, f):
    n = len(C)
    Res = []*n
    for i in range(n):
        Res.append([0]*n)
    for i in range(n):
        for j in range(n):
            #No grafo residual apenas diminuimos da capacidade a quantidade indicada pelo fluxo
            Res[i][j] = C[i][j] - f[i][j]
    return Res

def FordFulkerson(C, s, t):
    f = []
    n = len(C)
    for i in range(n):
        line = [0]*n
        f.append(line.copy())
    #Inicializamos o primeiro grafo residual (não há fluxo então é o mesmo Grafo)
    Res = ResidualNetwork(C, f)
    #Encontramos o caminho
    hasPath, path = FindPath(Res, s, t)
    while(hasPath):
        #Resgatamos a capacidade mínima do caminho
        minC = INFINITY
        p = len(path)-1
        for i in range(p):
            if(Res[path[i]][path[i+1]] < minC):
                minC = Res[path[i]][path[i+1]]
        #Atualizamos o fluxo de ida e volta para cada aresta do caminho
        for i in range(p):
            #Para a aresta indo somamos o fluxo
            f[path[i]][path[i+1]] += minC
            #Para a aresta voltando diminuímos
            f[path[i+1]][path[i]] = -1*(f[path[i]][path[i+1]])
        #Recalculamos o grafo residual
        Res = ResidualNetwork(C, f)
        #Procuramos um novo caminho
        hasPath, path = FindPath(Res, s, t)
    totalFlux = 0
    for i in range(len(f)):
        #Acumulamos todo o fluxo saindo da origem
        totalFlux += f[s][i]
    return f, totalFlux

C, s, t = readFile()
f, totalFlux = FordFulkerson(C, s, t)
print("Final Flux Matrix:")
PrintMatrix(f)
print()
print(f"Total Flux from {s} to {t}: {totalFlux}")