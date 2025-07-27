#Lê uma matriz de adjacência a partir de um arquivo .txt e converte em uma estrutura utilizável.
def read_graph_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    matrix = [list(map(float, line.strip().strip('[],').split(','))) for line in lines if line.strip()]
    n = len(matrix)
    return n, matrix
