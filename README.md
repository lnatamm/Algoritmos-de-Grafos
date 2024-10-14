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
>𝑟 - A fonte da árvore do algoritmo de Bellman-Ford

# [2 - Kruskal](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/Kruskal) 
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

# [3 - Prim](https://github.com/lnatamm/Algoritmos-de-Grafos/tree/main/Prim) 
## [main.py](https://github.com/lnatamm/Algoritmos-de-Grafos/blob/main/Prim/main.py) - Implementação do Bellman-Ford
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
> 𝑟 - A raiz da árvore do algoritmo de Prim