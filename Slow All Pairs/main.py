import os

INF = 999999

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

#Lê a matriz de adjacência do arquivo "allpairs.txt"
def readFile():
    filePath = os.getcwd() + "\\Slow All Pairs\\allpairs.txt"
    file = open(filePath)
    N = file.readline()
    N = removeLineBreak(N)
    W = []

    for i in range(N):
        w.append([])
        line = file.readline().split()
        for j in range(N):
            W[i].append(float(line[j]))

    return W

#Printa cada linha de uma matriz M qualquer
def printMatrix(M):
    n = len(M)
    for i in range(n):
        print(M[i])

#Método que permite a soma de 2 números funcione caso um deles seja infinito
def sum(x, y):
    if x == INF or y == INF:
        return INF
    return x + y

#Método auxiliar
def extendShortestPaths(L, W, Pi):
    n = len(L)
    #Inicia uma matriz L' com todos seus valores infinitos
    l = []
    for i in range(n):
        line = [INF]*n
        l.append(line)
    #Loop para cada vértice i
    for i in range(n):
        #Loop para cada vértice j
        for j in range(n):
            if(i != j):
                #Loop para cada possível vértice intermediário k
                for k in range(n):
                    print(f"i: {i}")
                    print(f"j: {j}")
                    print(f"k: {k}")
                    print(f"l[{i}][{j}]: {l[i][j]}")
                    print(f"L[{i}][{k}]: {L[i][k]} ; W[{k}][{j}]: {W[k][j]}")
                    #Se o caminho ik, kj for menor que o caminho ij
                    if(l[i][j] > sum(L[i][k], W[k][j])):
                        #Atualizamos o caminho ij
                        l[i][j] = sum(L[i][k], W[k][j])
                        #O novo predecessor do vértice j é o vértice intermediário k
                        Pi[i][j] = k+1
                    print("l:")
                    printMatrix(l)
    
    return l, Pi

def definePi(W):
    n = len(W)
    Pi = []
    for i in range(n):
        Pi.append([])
        for j in range(n):
            if(i != j and W[i][j] != INF):
                Pi[i].append(i)
            else:
                Pi[i].append(-1)
    return Pi


def SlowAllPairs(W):
    n = len(W)
    L = [[]]*n
    Pi = definePi(W)
    for i in range(n):
        line = []
        for j in range(n):
            line.append(W[i][j])
        L[0].append(line)

    for m in range(n-2):
        print(f"L{m}: ")
        printMatrix(L[m])
        L[m+1], Pi = extendShortestPaths(L[m], W, Pi)
        print(f"L{m+1}: ")
    printMatrix(L[n-2])
    return L[n-2], Pi

W = readFile()
L, Pi = SlowAllPairs(W)
print("L:")
printMatrix(L)
print("Pi:")
printMatrix(Pi)