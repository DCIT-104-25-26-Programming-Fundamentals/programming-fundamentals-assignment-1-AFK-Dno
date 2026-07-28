# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    for row in matrix:
        print("".join(f"{val:>6}" for val in row))
    print()

def read_matrix(rows, cols, name="Matrix"):
    print(f"\nEntering {name} ({rows}x{cols}):")    
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i + 1}: ").split()))
                if len(row) != cols:
                    print(f"Error: Row must contain exactly {cols} numbers. Try again.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: Invalid input. Please enter integers separated by spaces.")
    return matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

def multiply_matrices(matrix_a, matrix_b):
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

def main():
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    
    choice = input("\nSelect an operation (1, 2, or 3): ").strip()
    
    if choice == '1':
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        matrix = read_matrix(rows, cols)
        
        print("\nOriginal Matrix:")
        print_matrix(matrix)
        
        transposed = transpose_matrix(matrix)
        print("Transposed Matrix:")
        print_matrix(transposed)

    elif choice == '2':
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        print("\nMatrix A:")
        matrix_a = read_matrix(rows, cols)
        print("\nMatrix B:")
        matrix_b = read_matrix(rows, cols)
        
        sum_result = add_matrices(matrix_a, matrix_b)
        print("\nResult Matrix:")
        print_matrix(sum_result)

    elif choice == '3':
        m = int(input("Enter number of rows for Matrix A: "))
        n = int(input("Enter number of columns for Matrix A / rows for Matrix B: "))
        p = int(input("Enter number of columns for Matrix B: "))
        
        print("\nMatrix A:")
        matrix_a = read_matrix(m, n)
        print("\nMatrix B:")
        matrix_b = read_matrix(n, p)
        
        prod_result = multiply_matrices(matrix_a, matrix_b)
        print("\nResult Matrix:")
        print_matrix(prod_result)


if __name__ == "__main__":
    main()
