def print_matrix(matrix):
    """
    Prints a given matrix with elements formatted to three decimal places.

    Parameters:
    matrix (list of list of float): The matrix to be printed.
    """
    for row in matrix:
        formatted_row = [f"{elem:.3f}" for elem in row]
        print("(" + ", ".join(formatted_row) + ")")


def create_matrix(size):
    """
    Creates an identity matrix of given size.

    Parameters:
    size (int): The size of the matrix to be created.

    Returns:
    list of list of float: An identity matrix of the given size.
    """
    identity = [[0.0] * size for _ in range(size)]
    for i in range(size):
        identity[i][i] = 1.0
    return identity


def inverse_matrix(matrix):
    """
    Finds the inverse of a given square matrix using elementary row operations.

    Parameters:
    matrix (list of list of float): The matrix to be inverted.

    Returns:
    list of list of float: The inverse of the given matrix.
    """
    size = len(matrix)
    identity = create_matrix(size)
    matrix_copy = [row[:] for row in matrix]

    for i in range(size):
        factor = matrix_copy[i][i]
        for j in range(size):
            matrix_copy[i][j] /= factor
            identity[i][j] /= factor

        for k in range(size):
            if k != i:
                factor = matrix_copy[k][i]
                for j in range(size):
                    matrix_copy[k][j] -= factor * matrix_copy[i][j]
                    identity[k][j] -= factor * identity[i][j]

    return identity


def decomposition(matrix):
    """
    Performs LU decomposition of a given square matrix.

    Parameters:
    matrix (list of list of float): The matrix to be decomposed.

    Returns:
    tuple: Two matrices, lower and upper, representing the LU decomposition of the given matrix.
    """
    size = len(matrix)
    lower = [[0.0] * size for _ in range(size)]
    upper = [[0.0] * size for _ in range(size)]

    for i in range(size):
        lower[i][i] = 1.0
        for j in range(i, size):
            upper[i][j] = matrix[i][j] - sum(lower[i][k] * upper[k][j] for k in range(i))
        for j in range(i + 1, size):
            if upper[i][i] == 0:
                upper[i][i] = 1e-10  # Avoid division by zero
            lower[j][i] = (matrix[j][i] - sum(lower[j][k] * upper[k][i] for k in range(i))) / upper[i][i]

    return lower, upper


def forward_substitution(lower, b):
    """
    Solves the system of linear equations Ly = b using forward substitution.

    Parameters:
    lower (list of list of float): The lower triangular matrix L.
    b (list of float): The right-hand side vector b.

    Returns:
    list of float: The solution vector y.
    """
    size = len(b)
    y = [0.0] * size
    for i in range(size):
        y[i] = b[i] - sum(lower[i][j] * y[j] for j in range(i))
    return y


def backward_substitution(upper, y):
    """
    Solves the system of linear equations Ux = y using backward substitution.

    Parameters:
    upper (list of list of float): The upper triangular matrix U.
    y (list of float): The solution vector y from forward substitution.

    Returns:
    list of float: The solution vector x.
    """
    size = len(y)
    x = [0.0] * size
    for i in range(size - 1, -1, -1):
        x[i] = (y[i] - sum(upper[i][j] * x[j] for j in range(i + 1, size))) / upper[i][i]
    return x


def solution(matrix, b):
    """
    Solves the system of linear equations Ax = b using LU decomposition and substitution.

    Parameters:
    matrix (list of list of float): The coefficient matrix A.
    b (list of float): The right-hand side vector b.

    Returns:
    list of float: The solution vector x.
    """
    lower, upper = decomposition(matrix)
    y = forward_substitution(lower, b)
    x = backward_substitution(upper, y)
    return x


def main():
    """
    The main function to demonstrate finding the inverse of a matrix and solving a system of linear equations.
    """
    matrix = [[1, 4, -3], [-2, 1, 5], [3, 2, 1]]
    b = [1, 1, 1]

    # Part A: Finding the inverse matrix of A
    inverse = inverse_matrix(matrix)
    print("Inverse matrix of A:")
    print_matrix(inverse)

    # Part B: Solving the system of equations Ax = b
    solution_vector = solution(matrix, b)
    formatted_solution = [f"{elem:.3f}" for elem in solution_vector]
    print("\nSolution vector X:")
    print("(" + ", ".join(formatted_solution) + ")")


if __name__ == "__main__":
    main()