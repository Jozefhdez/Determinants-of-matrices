# Initialize variables
rows_matrix = 0
columns_matrix = 0
determinant = 0

# Ask the user for the number of rows and columns of the matrix
print("Select the number of rows for the matrix: ")
rows_matrix = int(input())
print("Select the number of columns for the matrix: ")
columns_matrix = int(input())

# Create an empty matrix
matrix = [[0 for _ in range(columns_matrix)] for _ in range(rows_matrix)]

# Input values for the matrix
print("Enter values for the matrix:")
for i in range(rows_matrix):
    for j in range(columns_matrix):
        matrix[i][j] = int(input(f"Enter the value for position ({i+1}, {j+1}): "))
print("")

# Check if it is a square matrix, and if so, calculate the determinant based on its size
if rows_matrix == columns_matrix:
    if rows_matrix == 1:
        print(matrix)
        print(f"The determinant is: {matrix[0][0]}.")
    elif rows_matrix == 2:
        print(matrix)
        print(f"The determinant is: {matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]}.")
    elif rows_matrix == 3:
        print(matrix)
        det = (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )
        print(f"The determinant is: {det}.")
    elif rows_matrix == 4:
        print(matrix)
        det = (
            matrix[0][0] * (
                matrix[1][1] * (matrix[2][2] * matrix[3][3] - matrix[2][3] * matrix[3][2]) -
                matrix[1][2] * (matrix[2][1] * matrix[3][3] - matrix[2][3] * matrix[3][1]) +
                matrix[1][3] * (matrix[2][1] * matrix[3][2] - matrix[2][2] * matrix[3][1])
            ) -
            matrix[0][1] * (
                matrix[1][0] * (matrix[2][2] * matrix[3][3] - matrix[2][3] * matrix[3][2]) -
                matrix[1][2] * (matrix[2][0] * matrix[3][3] - matrix[2][3] * matrix[3][0]) +
                matrix[1][3] * (matrix[2][0] * matrix[3][2] - matrix[2][2] * matrix[3][0])
            ) +
            matrix[0][2] * (
                matrix[1][0] * (matrix[2][1] * matrix[3][3] - matrix[2][3] * matrix[3][1]) -
                matrix[1][1] * (matrix[2][0] * matrix[3][3] - matrix[2][3] * matrix[3][0]) +
                matrix[1][3] * (matrix[2][0] * matrix[3][1] - matrix[2][1] * matrix[3][0])
            ) -
            matrix[0][3] * (
                matrix[1][0] * (matrix[2][1] * matrix[3][2] - matrix[2][2] * matrix[3][1]) -
                matrix[1][1] * (matrix[2][0] * matrix[3][2] - matrix[2][2] * matrix[3][0]) +
                matrix[1][2] * (matrix[2][0] * matrix[3][1] - matrix[2][1] * matrix[3][0])
            )
        )
        print(f"The determinant is: {det}.")

else:
    print("Cannot calculate the determinant as it is not a square matrix.")
    exit()
