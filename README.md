# Algoritmos de Grafos
Implementação de diversos algoritmos pra grafos

# [1 - Bellman-Ford](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/Bellman-Ford) 
## [main.py](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Bellman-Ford/main.py) - Implementação do Bellman-Ford
>### Saída 
>
> 𝑃𝑖, um array de 𝑁 elementos com o predecessor de cada vértice
>
> 𝑑, um array de 𝑁 elementos com as distâncias de cada vértice à fonte 𝑟
## [bf.txt](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Bellman-Ford/bf.txt) - Arquivo de entrada do algoritmo
> ### Entrada
> 𝑁 - O número de vértices, que são nomeados de 0 a 𝑁 − 1
>
> A matriz de adjacência, com elementos separados por espaços  
>- A matriz de adjacência tem entradas 0 na linha 𝑖 e coluna 𝑗 se não há arestas entre os vértices 𝑖 e 𝑗. Caso contrário,
>o valor é o peso (positivo) da aresta.
>
> Exemplo:
>
>| | | | |
>|---|---|---|---|
>| 4 |
>| 0 | 1 | 2.5 | 0 |
>| 1 | 0 | 1.5 | 2 |
>| 2.5 | 1.5 | 0 | 0 |
>| 0 | 2 | 0 | 0 |
>
>0
>
>𝑟 - A fonte da árvore do algoritmo de Bellman-Ford

# [2 - BFS (Breadth-First Search) ou Busca em Largura](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/BFS)
## [main.py](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/BFS/main.py) - Implementação do BFS
>### Saída 
>
> 𝑃𝑖, um array de 𝑁 elementos com o predecessor de cada vértice
>
> 𝑑, um array de 𝑁 elementos com as distâncias de cada vértice à fonte 𝑟
## [bfs.txt](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/BFS/bfs.txt) - Arquivo de entrada do algoritmo
> ### Entrada
> 𝑁 - O número de vértices, que são nomeados de 0 a 𝑁 − 1
>
> A matriz de adjacência, com elementos separados por espaços  
>- A matriz de adjacência tem entradas 0 na linha 𝑖 e coluna 𝑗 se não há arestas entre os vértices 𝑖 e 𝑗. Caso contrário,
>o valor é 1.
>
> Exemplo:
>
>| | | | |
>|---|---|---|---|
>| 4 |
>| 0 | 1 | 1 | 0 |
>| 1 | 0 | 1 | 1 |
>| 1 | 1 | 0 | 0 |
>| 0 | 1 | 0 | 0 |
>
>0
>
>𝑟 - A fonte da árvore do algoritmo de BFS
# [3 - Bipartite](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/Bipartite)
## [main.py](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Bipartite/main.py) - Implementação do BFS
>### Saída 
>
> Retorna se o grafo é bipartido ou não
> - Caso o grafo seja bipartido:
> 1. Imprime a mensagem "Sim, e suas partes são:"
> 2. Imprime uma parte do grafo
> 3. Imprime a outra parte do grafo
> - Caso o grafo não seja bipartido:
> 1. Imprime a mensagem "Não, pois" seguido da lista com os ciclos ímpares do grafo "formam ciclo ímpar"
## [matriz.txt](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Bipartite/matriz.txt) - Arquivo de entrada do algoritmo
> ### Entrada
> 𝑁 - O número de vértices, que são nomeados de 0 a 𝑁 − 1
>
> A matriz de adjacência, com elementos separados por espaços  
>- A matriz de adjacência tem entradas 0 na linha 𝑖 e coluna 𝑗 se não há arestas entre os vértices 𝑖 e 𝑗. Caso contrário,
>o valor é 1.
>
> Exemplo:
>
>| | | | |
>|---|---|---|---|
>| 4 |
>| 0 | 1 | 1 | 0 |
>| 1 | 0 | 1 | 1 |
>| 1 | 1 | 0 | 0 |
>| 0 | 1 | 0 | 0 |
# [4 - DFS (Depth-First Search) ou Busca em profundidade](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/Bipartite)
## [main.py](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/DFS/main.py) - Implementação do DFS
>### Saída 
>discovery, um array de 𝑁 elementos com o tempo de descoberta de cada vértice
>
>finalization, um array de 𝑁 elementos com o tempo de finalização de cada vértice
>
> 𝑃𝑖, um array de 𝑁 elementos com o predecessor de cada vértice
>
> 𝑑, um array de 𝑁 elementos com as distâncias de cada vértice a cada uma de suas raízes ([distância até sua raiz], [sua raiz])
>
>state, um array de 𝑁 elementos com os estados de cada vértice. 0: Não descoberto; 1: Visitado; 2: Finalizado. Caso existe algum vértice não descoberto, o grafo é desconexo
>
>root, um array de 𝑁 elementos com as raízes de cada vértice
## [matriz.txt](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/DFS/dfs.txt) - Arquivo de entrada do algoritmo
> ### Entrada
> 𝑁 - O número de vértices, que são nomeados de 0 a 𝑁 − 1
>
> A matriz de adjacência, com elementos separados por espaços  
>- A matriz de adjacência tem entradas 0 na linha 𝑖 e coluna 𝑗 se não há arestas entre os vértices 𝑖 e 𝑗. Caso contrário,
>o valor é 1.
>
> Exemplo:
>
>| | | | |
>|---|---|---|---|
>| 4 |
>| 0 | 1 | 1 | 0 |
>| 1 | 0 | 1 | 1 |
>| 1 | 1 | 0 | 0 |
>| 0 | 1 | 0 | 0 |
# [5 - Kruskal](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/Kruskal) 
## [main.py](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Kruskal/main.py) - Implementação do Kruskal
>### Saída
>
> Retorna "VERDADEIRO" "e em um array de 𝑁 − 1 elementos com as arestas da árvore, caso o grafo seja conexo 
>
> Retorna "FALSO" caso o grafo seja desconexo
## [kruskal.txt](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Kruskal/kruskal.txt) - Arquivo de entrada do algoritmo
>### Entrada
>
> 𝑁, o número de vértices, que são nomeados de 0 a 𝑁 − 1
>
> A matriz de adjacência, com elementos separados por espaços  
>- A matriz de adjacência tem entradas 0 na linha 𝑖 e coluna 𝑗 se não há arestas entre os vértices 𝑖 e 𝑗. Caso contrário,
o valor é o peso (positivo) da aresta.
>
> Exemplo:
>
>| | | | |
>|---|---|---|---|
>| 4 |
>| 0 | 1 | 2.5 | 0 |
>| 1 | 0 | 1.5 | 2 |
>| 2.5 | 1.5 | 0 | 0 |
>| 0 | 2 | 0 | 0 |

# [6 - Prim](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/Prim) 
## [main.py](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Prim/main.py) - Implementação do Prim
>### Saída
> Retorna "VERDADEIRO" e em um array 𝑃 𝑖 de 𝑁 elementos com os predecessores de cada vértice, caso o grafo seja
conexo
>
>
> Retorna "FALSO" caso o grafo seja desconexo
## [prim.txt](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Prim/prim.txt) - Arquivo de entrada do algoritmo
>### Entrada
>
> 𝑁, o número de vértices, que são nomeados de 0 a 𝑁 − 1
>
> A matriz de adjacência, com elementos separados por espaços  
>- A matriz de adjacência tem entradas 0 na linha 𝑖 e coluna 𝑗 se não há arestas entre os vértices 𝑖 e 𝑗. Caso contrário,
o valor é o peso (positivo) da aresta.
>
> Exemplo:
>
>| | | | |
>|---|---|---|---|
>| 4 |
>| 0 | 1 | 2.5 | 0 |
>| 1 | 0 | 1.5 | 2 |
>| 2.5 | 1.5 | 0 | 0 |
>| 0 | 2 | 0 | 0 |
>
>0
>
> 𝑟 - A raiz da árvore do algoritmo de Prim
# [7 - Ford-Fulkerson](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/Ford-Fulkerson)
## [main.py](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Ford-Fulkerson/main.py) - Implementação do Ford-Fulkerson
>### Saída 
>
> 𝘧, uma matriz com o fluxo final de cada aresta do grafo
>
> totalFlux, um inteiro que indica o fluxo máximo que pode sair da fonte u
## [ff.txt](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Ford-Fulkerson/ff.txt) - Arquivo de entrada do algoritmo
> ### Entrada
> 𝑁 - O número de vértices, que são nomeados de 0 a 𝑁 − 1
>
> A matriz de adjacência, com elementos separados por espaços  
>- A matriz de adjacência recebe a capacidade de cada aresta ij.
>
> Exemplo:
>
>| | | | | | |
>|---|---|---|---|---|---|
>| 6 |
>| 0 | 3 | 0 | 0 | 0 | 2 | 
>| 0 | 0 | 2 | 0 | 0 | 0 |
>| 0 | 1 | 0 | 1 | 0 | 0 |
>| 0 | 0 | 5 | 0 | 4 | 0 |
>| 0 | 0 | 0 | 3 | 0 | 2 |
>| 3 | 0 | 0 | 0 | 4 | 0 |
>
>0 3
>
>𝘴, 𝘵 - A fonte o sumidouro, respectivamente.