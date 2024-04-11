def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty result matrix with swapped dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate through the original matrix and copy elements to the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

def main():
    try:
        # Example matrix
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # Transpose the matrix
        transposed_matrix = transpose_matrix(matrix)

        # Print the original and transposed matrices
        print("Original Matrix:")
        for row in matrix:
            print(row)

        print("\nTransposed Matrix:")
        for row in transposed_matrix:
            print(row)

    except IndexError:
        print("Please ensure the matrix is non-empty and rectangular.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
 