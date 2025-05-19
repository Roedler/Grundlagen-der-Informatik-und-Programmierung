def multiplication_table(max_x, max_y):
    max_value = max_x * max_y
    cell_width = len(str(max_value)) + 1
    print(" " * cell_width + "  ", end="")
    for x in range(1, max_x + 1):
        print(f"{x:>{cell_width}}", end=" ")
    print()
    print(" " * cell_width + " ┌" + "─" * (cell_width * max_x + max_x - 1) + "─┐")
    for y in range(1, max_y + 1):
        print(f"{y:>{cell_width}} │", end="")
        for x in range(1, max_x + 1):
            print(f"{x * y:>{cell_width}}", end=" ")
        print("│")
    print(" " * cell_width + " └" + "─" * (cell_width * max_x + max_x - 1) + "─┘")

max_x = int(input("Enter the maximum column number (x): "))
max_y = int(input("Enter the maximum row number (y): "))
multiplication_table(max_x, max_y)
