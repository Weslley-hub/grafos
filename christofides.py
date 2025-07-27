import networkx as nx
from collections import defaultdict




#Constrói uma Árvore Geradora Mínima a partir de uma matriz de adjacência utilizando o algoritmo de Prim
def prim_mst(matrix):   
    n = len(matrix)
    selected = [False] * n
    selected[0] = True

    edges = []

    while len(edges) < n - 1:
        min_edge = (None, None, float('inf'))

        for u in range(n):
            if selected[u]:
                for v in range(n):
                    if not selected[v] and 0 < matrix[u][v] < min_edge[2]:
                        min_edge = (u, v, matrix[u][v])

        u, v, weight = min_edge
        selected[v] = True
        edges.append((u, v))

    return edges

#Identifica os vértices com grau ímpar em uma árvore geradora mínima
def find_odd_degree_vertices(mst_edges):
    from collections import defaultdict

    degree = defaultdict(int)

    for u, v in mst_edges:
        degree[u] += 1
        degree[v] += 1

    odd_vertices = [v for v, d in degree.items() if d % 2 == 1]
    return odd_vertices

# Calcula um emparelhamento perfeito de custo mínimo entre os vértices de grau ímpar,
#Aqui estou usando a biblioteca externa NETWORKX
def minimum_weight_perfect_matching(odd_vertices, matrix):
    G = nx.Graph()

    for i in range(len(odd_vertices)):
        for j in range(i + 1, len(odd_vertices)):
            u = odd_vertices[i]
            v = odd_vertices[j]
            weight = matrix[u][v]
            G.add_edge(u, v, weight=weight)

    matching = nx.algorithms.matching.min_weight_matching(G)

    return list(matching)


#Combina as arestas da árvore geradora mínima, com as do emparelhamento perfeito mínimo,
#formando um multigrafo em que todos os vértices possuem grau par
def combine_graphs(mst_edges, matching_edges):
    multigraph = defaultdict(list)

    for u, v in mst_edges:
        multigraph[u].append(v)
        multigraph[v].append(u)

    for u, v in matching_edges:
        multigraph[u].append(v)
        multigraph[v].append(u)

    return multigraph  

#Determina um ciclo euleriano em um multigrafo onde todos os vértices têm grau par,
#Implementa o algoritmo de Hierholzer
def find_eulerian_tour(multigraph):
    from collections import defaultdict, deque
    import copy

    graph = copy.deepcopy(multigraph)
    tour = []
    stack = [next(iter(graph))] 
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            stack.append(v)
        else:
            tour.append(stack.pop())

    tour.reverse()
    return tour


#Converte um ciclo euleriano em um ciclo hamiltoniano,
#elimina visitas repetidas a vértices já percorridos.
def shortcut_eulerian_to_hamiltonian(euler_tour):
    visited = set()
    path = []

    for v in euler_tour:
        if v not in visited:
            visited.add(v)
            path.append(v)

    path.append(path[0])
    return path

#Calcula o custo total de um ciclo hamiltoniano com base na matriz de adjacência
def calculate_cost(path, matrix):
    cost = 0
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        cost += matrix[u][v]
    return cost

#Executa o Algoritmo de Christofides para encontrar uma solução aproximada do Problema do Caixeiro Viajante Métrico
def christofides(matrix):
    mst_edges = prim_mst(matrix)
    odd_vertices = find_odd_degree_vertices(mst_edges)
    matching_edges = minimum_weight_perfect_matching(odd_vertices, matrix)
    multigraph = combine_graphs(mst_edges, matching_edges)
    euler_tour = find_eulerian_tour(multigraph)
    hamiltonian = shortcut_eulerian_to_hamiltonian(euler_tour)
    cost = calculate_cost(hamiltonian, matrix)
    return hamiltonian, cost