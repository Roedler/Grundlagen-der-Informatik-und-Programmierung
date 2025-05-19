print("Input an m x n matrix and display its transpose:")

while True:
    rows = int(input("Number of rows (n): "))
    cols = int(input("Number of columns (m): "))

    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            element = input(f"a({i + 1}, {j + 1}) = ")
            row.append(element)
        matrix.append(row)

    print("\nThe list you entered is:")
    print(matrix)

    print("\nThe matrix you entered is:")
    for row in matrix:
        print(" ".join(row))

    print("\nThe transpose of the matrix is:")
    for j in range(cols):
        transposed_row = [matrix[i][j] for i in range(rows)]
        print(" ".join(transposed_row))

    again = input("\nDo you want to enter another matrix? (Y/N): ").strip().lower()
    if again != 'y':
        break

print("\nThe program was executed by Lennart Novak.")