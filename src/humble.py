#export
#this cell will be tested
def hello():
    return "hello"#export
def init_mat(nrows, ncols):
    M = []
    while len(M) < nrows:
        M.append([])
        while len(M[-1]) < ncols:
            M[-1].append(0.0)
 
    return M

init_mat(3,4)#export
def add(A,B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')
 
    # Section 2: Create a new matrix for the matrix sum
    C = init_mat(rowsA, colsB)
 
    # Section 3: Perform element by element sum
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] + B[i][j]
 
    return C
