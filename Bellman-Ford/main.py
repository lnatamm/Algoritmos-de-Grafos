import os

INFINITY = 1000000

def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

def readFile():
    filePath = os.getcwd() + "\\bf.txt"
    file = open(filePath)
    N = file.readline()
    N = removeLineBreak(N)
    G = []

    for i in range(N):
        G.append([])
        line = file.readline().split()
        for j in range(N):
            G[i].append(int(line[j]))

    r = file.readline()
    r = removeLineBreak(r)
    return G, r

def initializeSingleSource(G, s):
    n = len(G)
    d[INFINITY]*n
    Pi[-1]*n
    d[s] = 0
    return d, Pi

def sum(x, y):
    if(x == INFINIY or y == INFINITY):
        return INFINIY
    return x + y

def relax(d, Pi, u, v, G):
    if(d[v] > sum(d[u], G[u][v])):
        d[v] = sum(d[u], G[u][v])
        Pi[v] = u
    return d, Pi

def bellmanFord(G, s):

    n = len(G)
    d, Pi = initializeSingleSource(G, s)
    
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if(G[u][v] > 0):
                    d, Pi = relax(d, Pi, u, v, G)

    return d, Pi

G, r = readFile()
d, Pi = bellmanFord(G, r)
print("Pi:")
print(Pi)
print("d:")
print(d)