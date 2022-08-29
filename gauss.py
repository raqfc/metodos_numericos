##########
# Pivoteamento parcial
# matrix: matriz mxn a ser pivoteada
# startLine: Linha em que se deve comecar o pivoteamento
# column: indice (coluna) a ser pivoteada
#
# retorna a matriz pivoteada
def matrix_pivoting(matrix, startLine, column):
    lines = len(matrix)
    for i in range(startLine, lines):
        for lineIndex in range(startLine + 1, lines):
            if matrix[lineIndex][column] > matrix[lineIndex - 1][column]:
                matrix[lineIndex], matrix[lineIndex - 1] = matrix[lineIndex - 1], matrix[lineIndex]

    # matrix.sort(key=lambda line: line[index])
    return matrix


##########
# Solucao de Sistema triangular inferior
# a: matriz alvo mxn de coeficientes
# b: matriz solucao mx1 (matriz linha)
#
# dado [a][x]=[b], a função retorna a matriz linha solucao [x]
# retorna o vetor [x]
def lower_triangular_matrix_solve(a, b):
    lines = len(a)

    x = [0 for i in range(lines)]

    x[0] = b[0] / a[0][0]

    for k in range(1, lines):
        s = 0
        for j in range(0, k - 1):
            s += a[k][j]
        x[k] = (b[k] - s) / a[k][k]

    return x


##########
# Eliminação de Gauss
# a: matriz alvo mxn de coeficientes
# b: matriz solucao mx1 (matriz linha)
#
# dado [a][x]=[b], a função retorna a matriz linha solucao [x]
# retorna o vetor
def gauss_elimination(a, b):
    lines = len(a)
    columns = len(a[0])




def print_matrix(matrix, name='matrix'):
    print(name, ' :')
    for line in matrix:
        print('  ', line)
    print(' ')
