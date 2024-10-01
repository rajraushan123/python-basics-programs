def print_diamond(rows):
    # Upper pyramid
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
    # Lower inverted pyramid
    for i in range(rows - 2, -1, -1):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

n = int(input("Enter the number of rows: "))
print_diamond(n)
