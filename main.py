# Este arquivo executa o Algoritmo de Christofides em uma instância do TSP
# A entrada deve estar em formato de matriz de adjacência em um arquivo .txt
# A saída será o ciclo hamiltoniano encontrado e seu custo total

from utils import read_graph_from_file
from christofides import christofides

if __name__ == "__main__":
    #escolha a matriz de adjacência que deseja executar
    n, matrix = read_graph_from_file("inputs/bayg29.tsp.txt")
    path, cost = christofides(matrix)


    #exibe o resultado
    print("Ciclo Hamiltoniano:", path)
    print("Custo total:", cost)
