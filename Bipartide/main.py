INFINITY = 999999
G = [
    [0, 1, 1, 0, 0, 0],  # Vértice 0
    [0, 1, 1, 0, 0, 0],  # Vértice 1
    [1, 0, 0, 1, 1, 0],  # Vértice 2
    [1, 0, 0, 0, 0, 1],  # Vértice 3
    [0, 1, 0, 1, 0, 0],  # Vértice 4
    [0, 0, 1, 0, 1, 0],  # Vértice 5
]
#Realiza a visita do vértice dentro do dfs
def DFSvisit(u, d, Pi, state, root, bipartide, cycle, nCycles, nonBipartiteCycles):
    #Tamanho de G
    n = len(G)
    #Altera o estado do vértice v para visitado
    state[u] = 1
    #Loop para cada vizinho de v
    for v in range(n):
        #Se o vértice ainda não foi visitado
        if(G[u][v] == 1):
            if(state[v] == 0):
                #A raiz de v é a mesma que a de u
                root[v] = root[u]
                #A distância de v para a raiz é a distância de u + 1
                d[v] = [root[u], d[u][1] + 1]
                #O predecessor de v é u
                Pi[v] = u
                #Atualiza os valores de todos os parametros e é feita a visitação do vértice v
                d, Pi, state, root, bipartide, cycle, nCycles, nonBipartiteCycles = DFSvisit(v, d, Pi, state, root, bipartide, cycle, nCycles, nonBipartiteCycles)
            elif(state[v] == 1 and Pi[u] != v and root[v] == root[u] and u != v):
                aux = u
                cycle[nCycles].append(aux)
                while(aux != v):
                    aux = Pi[aux]
                    cycle[nCycles].append(aux)
                if(len(cycle[nCycles]) % 2 != 0):
                    bipartide = False
                    nonBipartiteCycles.append(cycle[nCycles])
                nCycles = nCycles + 1
                cycle.append([])
    #Após todos os vizinhos de u terem sido visitados, finalizamos o vértice v
    state[u] = 2
    #Retorna todos os parâmetros atualizados
    return d, Pi, state, root, bipartide, cycle, nCycles, nonBipartiteCycles

def IsBipartite(G):
    #Tamanho de G
    n = len(G)
    #Inicializa o array com as distâncias de cada vértice para cada raiz
    d = [[-1, 0]]*n
    #Inicializa o array com os predecessores de cada vértice
    Pi = [-1]*n
    #Inicializa os estados de cada vértice. 0: Não visitado; 1: Visitado; 2: Finalizado
    state = [0]*n
    #Inicializa as raizes de cada vértice como -1
    root = [-1]*n
    bipartide = True
    cycle = [[]]
    nCycles = 0
    nonBipartiteCycles = []
    #Loop para cada vértice u
    for u in range(n):
        #Se o vértice ainda não foi visitado
        if state[u] == 0:
            #A raiz do vértice u é ele mesmo
            root[u] = u
            #A distância do vértice u para a raiz (ele mesmo) é 0
            d[u] = [root[u], 0]
            #Atualiza os valores de todos os atributos e é feita a visitação do vértice u
            d, Pi, state, root, bipartide, cycle, nCycles, nonBipartiteCycles = DFSvisit(u, d, Pi, state, root, bipartide, cycle, nCycles, nonBipartiteCycles)

    #Retorna os tempos de descoberta, tempos de finalização, distâncias para as raízes, predecessores, estados e as raízes        
    return bipartide, nonBipartiteCycles
bipartide, nonBipartiteCycles = IsBipartite(G)
if(bipartide):
    print("Sim, e suas partes são: ")
else:
    print("Não ")