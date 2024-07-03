
A = [
    [1, -1, -2],
    [2, -3, -5],
    [-1, 3, 5]
]


def create_matrix(size):
    """
    Creates an matrix of a given size.

    Parameters:
    size (int): The size of the matrix (number of rows and columns).

    Returns:
    Determinant of the matrix.
    """
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


def horizontal_matrix_union(A, B):
    """
    Concatenates two matrices horizontally.

    Parameters:
    A (list of list of int/float): The first matrix.
    B (list of list of int/float): The second matrix.

    Returns:
    list of list of int/float: A new matrix formed by concatenating
    each row of matrix A with the corresponding row of matrix B.
    """
    return [row_a + row_b for row_a, row_b in zip(A, B)]


def replace_rows_in_matrix(matrix, row1, row2):
    """
    Swaps two rows in a given matrix.

    Parameters:
    matrix (list of list of int/float): The matrix in which rows will be swapped.
    row1 (int): The index of the first row to swap.
    row2 (int): The index of the second row to swap.

    Returns:
    None: The function modifies the matrix in place.
    """
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def scale_row(matrix, row, scale):
    """
    Scales a row in a given matrix by a specified factor.

    Parameters:
    matrix (list of list of int/float): The matrix containing the row to scale.
    row (int): The index of the row to scale.
    scale (int/float): The factor by which to scale the row.

    Returns:
    None: The function modifies the matrix in place.
    """
    matrix[row] = [scale * element for element in matrix[row]]


def add_scaled_row(matrix, source_row, target_row, scale):
    """
    Adds a scaled version of one row to another row in a given matrix.

    Parameters:
    matrix (list of list of int/float): The matrix containing the rows to modify.
    source_row (int): The index of the row to scale and add.
    target_row (int): The index of the row to which the scaled row will be added.
    scale (int/float): The factor by which to scale the source row.

    Returns:
    None: The function modifies the matrix in place.
    """
    matrix[target_row] = [
        target_element + scale * source_element
        for target_element, source_element in zip(matrix[target_row], matrix[source_row])
    ]


def inverse_matrix(A):
    """

    Calculates the inverse of a given matrix using methods we have learned

    Parameters:
    A (list of list of int/float): The square matrix to invert.

    Returns:
    list of list of int/float: The inverse of the matrix A.
    """
    size = len(A)
    I = create_matrix(size)
    AI = horizontal_matrix_union(A, I)

    for col in range(size):
        if AI[col][col] == 0:
            for row in range(col + 1, size):
                if AI[row][col] != 0:
                    replace_rows_in_matrix(AI, col, row)
                    break
            else:
                raise ValueError("The matrix is singular and cannot be inverted.")

        scale_row(AI, col, 1 / AI[col][col])

        for row in range(size):
            if row != col:
                add_scaled_row(AI, col, row, -AI[row][col])

    inverse = [row[size:] for row in AI]
    return inverse

def Matrixmultiplication(A, B):
    """
        Performs matrix multiplication of two matrices A and B.

        Parameters:
        A (list of list of int/float): The first square matrix.
        B (list of list of int/float): The second square matrix.

        Returns:
        list of list of int/float: The resulting matrix from multiplying A and B.
    """
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(size))
    return result

def calculate_matrix_infinity_norm(matrix):
    """
        Calculates the infinity norm (maximum row sum norm) of a given matrix.

        Parameters:
        matrix (list of list of int/float): The matrix for which to calculate the infinity norm.

        Returns:
        float: The infinity norm of the matrix.
        """
    return max(sum(abs(element) for element in row) for row in matrix)


def calculate_condition_number(matrix):
    """
        Calculates the condition number of a given matrix.

        Parameters:
        matrix (list of list of int/float): The matrix for which to calculate the condition number.

        Returns:
        float: The condition number of the matrix.
        """
    inv_matrix = inverse_matrix(matrix)
    infinity_norm_A = calculate_matrix_infinity_norm(matrix)
    infinity_norm_A_inverse = calculate_matrix_infinity_norm(inv_matrix)
    return infinity_norm_A * infinity_norm_A_inverse

A_inv = inverse_matrix(A)
product = Matrixmultiplication(A, A_inv)
Condition = calculate_condition_number(A)

print("Matrix A:")
for row in A:
    print(row)
print("\nInverse of A:")
for row in A_inv:
    print(row)
print("\nProduct of A and A^-1:")
for row in product:
    print(row)
print("\nCond:")
print(Condition)