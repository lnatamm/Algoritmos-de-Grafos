import os

#Definimos infinito como 1,000,000 por se tratar de um número suficientemente grande 
INFINITY = 1000000

def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

def readFile():
    filePath = os.getcwd() + "\\Bellman-Ford\\bf.txt"
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

#Inicializa os arrays d e 𝑃i
def initializeSingleSource(G, s):
    n = len(G)
    d = [INFINITY]*n
    Pi = [-1]*n
    d[s] = 0
    return d, Pi

#Método que permite a soma de 2 números funcione caso um deles seja infinito
def sum(x, y):
    if(x == INFINITY or y == INFINITY):
        return INFINITY
    return x + y

#Relaxa a aresta, atualizando a distância do vértice v para a fonte e alterando seu predescessor caso encontre um mais curto
def relax(d, Pi, u, v, G):
    #Se a distância atual de v para a fonte for maior que a soma entre a distância de u para a fonte com a aresta u,v
    if(d[v] > sum(d[u], G[u][v])):
        d[v] = sum(d[u], G[u][v])
        Pi[v] = u
    return d, Pi

#Retorna o array das distâncias de cada vértice e a lista de predecessores do caminho mínimo de G partindo de s
def bellmanFord(G, s):
    n = len(G)
    d, Pi = initializeSingleSource(G, s)
    #O algoritmo de Bellman-Ford necessita ser realizado N-1 vezes
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if(G[u][v] > 0):
                    #Relaxamos cada aresta do grafo
                    d, Pi = relax(d, Pi, u, v, G)
    return d, Pi

G, r = readFile()
d, Pi = bellmanFord(G, r)
print("Pi:")
print(Pi)
print("d:")
print(d)