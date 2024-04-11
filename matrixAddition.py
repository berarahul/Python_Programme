def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

# Example matrices
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]

# Add the matrices
result_matrix = add_matrices(matrix1, matrix2)

# Display the result
if result_matrix:
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nSum of the matrices:")
    for row in result_matrix:
        print(row)
else:
    print("Matrices have different dimensions, so addition is not possible.")
 