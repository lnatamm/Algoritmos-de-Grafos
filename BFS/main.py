import os

INFINITY = 1000000;

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

#Lê a matriz de adjacência do arquivo "bfs.txt"
def readFile():
    filePath = os.getcwd() + "\\BFS\\bfs.txt"
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

#Retorna o array das distâncias de cada vértice e a lista de predecessores de cada vértice de G partindo de r
def bfs(G, r):
    n = len(G);
    #Array que indica o estado de cada vértice. 0: Não visitado; 1: Visitado; 2: Finalizado
    state = [0]*n;
    #Array que indica os predecessores de cada vértice
    Pi = [-1]*n;
    #Array que indica a distância de cada vértice para a raiz r
    d = [INFINITY]*n;
    #Iniciamos a raiz como visitada já que partiremos dela
    state[r] = 1
    #A distância da raiz para ela mesma é 0
    d[r] = 0;
    #Predecessor da raiz vazio
    Pi[r] = -1;
    queue = [];
    #Primeiro vértice a ser observado será a raiz
    queue.append(r);
    #Até todos os vértices serem visitados
    while queue != []:
        #Armazena a o vértice da posição inicial da fila
        u = queue.pop();
        #Loop para cada vizinho de u
        for v in range(n):
            #Se o vizinho ainda não foi visitado
            if(G[u][v] == 1 and state[v] == 0):
                #Alteramos seu estado para visitado
                state[v] = 1;
                #Definimos o seu predecessor como u
                Pi[v] = u;
                #A sua distância para u é um nível maior que a distância de u para a raiz
                d[v] = 1 + d[u];
                #Agora iremos visitar o vértice v
                queue.append(v);
        #Após todos os vizinhos de u serem visitados alteramos seu estado para finalizado
        state[u] = 2;
    #Retornamos os predecessores e as distâncias
    return Pi, d;

G, r = readFile()
Pi, d = bfs(G, r)
print("Pi:")
print(Pi)
print("d:")
print(d)