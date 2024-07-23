
def check_dominant_diagonal(matrix):
    """
    Checks if the matrix has a dominant diagonal.

    Args:
    matrix -- A square matrix (list of lists).

    Returns:
    True if the matrix has a dominant diagonal, otherwise False.
    """
    for i in range(len(matrix)):
        sum_row = sum(abs(matrix[i][j]) for j in range(len(matrix)) if j != i)
        if abs(matrix[i][i]) <= sum_row:
            return False
    return True

def jacobi_method(matrix, vector, stop_criteria=0.001, max_iter=1000):
    """
    Solves the system of linear equations using the Jacobi method.

    Args:
    matrix -- Coefficient matrix (list of lists).
    vector -- Right-hand side vector (list).
    stop_criteria -- The tolerance for the stopping criterion.
    max_iter -- Maximum number of iterations.

    Returns:
    The solution vector (list) or None if the method does not converge.
    """
    n = len(vector)
    x_values = [0.0] * n
    if not check_dominant_diagonal(matrix):
        print("No dominant diagonal. Jacobi method may not converge.")
        return None
    print(f"{'Iteration':<10} {'x1':<10} {'x2':<10} {'x3':<10} {'Error':<10}")
    print(f"{0:<10} {x_values[0]:<10.4f} {x_values[1]:<10.4f} {x_values[2]:<10.4f} {'-':<10}")
    for iter_count in range(1, max_iter + 1):
        x_new = x_values.copy()
        for i in range(n):
            sigma = sum(matrix[i][j] * x_values[j] for j in range(n) if j != i)
            x_new[i] = (vector[i] - sigma) / matrix[i][i]
        error = max(abs(x_new[i] - x_values[i]) for i in range(n))
        print(f"{iter_count:<10} {x_new[0]:<10.4f} {x_new[1]:<10.4f} {x_new[2]:<10.4f} {error:<10.4f}")
        x_values = x_new
        if error < stop_criteria:
            break
    return x_values

def gauss_seidel_method(matrix, vector, stop_criteria=0.001, max_iter=1000):
    """
    Solves the system of linear equations using the Gauss-Seidel method.

    Args:
    matrix -- Coefficient matrix (list of lists).
    vector -- Right-hand side vector (list).
    stop_criteria -- The tolerance for the stopping criterion.
    max_iter -- Maximum number of iterations.

    Returns:
    The solution vector (list) or None if the method does not converge.
    """
    n = len(vector)
    x_values = [0.0] * n
    if not check_dominant_diagonal(matrix):
        print("No dominant diagonal. Gauss-Seidel method may not converge.")
        return None
    print(f"{'Iteration':<10} {'x1':<10} {'x2':<10} {'x3':<10} {'Error':<10}")
    print(f"{0:<10} {x_values[0]:<10.4f} {x_values[1]:<10.4f} {x_values[2]:<10.4f} {'-':<10}")
    for iter_count in range(1, max_iter + 1):
        x_old = x_values.copy()
        for i in range(n):
            sigma = sum(matrix[i][j] * x_values[j] for j in range(n) if j != i)
            x_values[i] = (vector[i] - sigma) / matrix[i][i]
        error = max(abs(x_values[i] - x_old[i]) for i in range(n))
        print(f"{iter_count:<10} {x_values[0]:<10.4f} {x_values[1]:<10.4f} {x_values[2]:<10.4f} {error:<10.4f}")
        if error < stop_criteria:
            break
    return x_values

# Example usage:
matrix = [
    [9, 1, 1],
    [2, 10, 3],
    [3, 4, 11]
]
vector = [10, 19, 0]

print("Jacobi Method:")
jacobi_result = jacobi_method(matrix, vector)
if jacobi_result:
    print(f"Solution: {jacobi_result}")

print("\nGauss-Seidel Method:")
gauss_seidel_result = gauss_seidel_method(matrix, vector)
if gauss_seidel_result:
    print(f"Solution: {gauss_seidel_result}")
