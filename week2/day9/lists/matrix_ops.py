def matrix_add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Matrix addition not possible due to dimension mismatch."
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Matrix multiplication not possible due to dimension mismatch."
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)] for row_a in A]

if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("Matrix A:", a)
    print("Matrix B:", b)
    print("Addition:", matrix_add(a, b))
    print("Transpose of A:", matrix_transpose(a))
    print("Multiplication:", matrix_multiply(a, b))

    c = [[1, 2, 3], [4, 5, 6]]
    d = [[7, 8], [9, 10], [11, 12]]

    print("\nMatrix C:", c)
    print("Matrix D:", d)
    print("Transpose of C:", matrix_transpose(c))
    print("Multiplication C x D:", matrix_multiply(c, d))