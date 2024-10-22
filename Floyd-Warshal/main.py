INF = 1000000

W = [
    [0, 3, 8, INF, -4],
    [INF, 0, INF, 1, 7],
    [INF, 4, 0, INF, INF],
    [2, INF, -5, 0, INF],
    [INF, INF, INF, 6, 0]
]

def printMatrix(M):
    n = len(M)
    for i in range(n):
        print(M[i])
    print()

def sum(x, y):
    if(x >= INF or y >= INF):
        return INF
    return x + y

def FloydWarshal(W):
    n = len(W)
    D = [[]]*(n+1)
    P0 = []
    Pi = [[]]*(n+1)

    for i in range(n):
        line = [-1]*n
        P0.append(line.copy())

    for i in range(n):
        D[0].append(W[i].copy())
        Pi[0].append(P0[0].copy())
    
    for i in range(n):
        for j in range(n):
            if(i != j and W[i][j] != INF):
                Pi[0][i][j] = i+1

    for i in range(n):
        D[i + 1] = D[0].copy()
        Pi[i + 1] = P0.copy()
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                soma = sum(D[k][i][k], D[k][k][j])
                if(D[k + 1][i][j] > soma):
                    D[k + 1][i][j] = soma
                    Pi[k + 1][i][j] = Pi[k][k][j]
                else:
                    D[k + 1][i][j] = D[k][i][j]
                    Pi[k + 1][i][j] = Pi[k][i][j]
    return D[n], Pi[n]

d, Pi = FloydWarshal(W)
printMatrix(d)
printMatrix(Pi)