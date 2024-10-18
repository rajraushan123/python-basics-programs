def hourglass(rows):
    # Inverted Pyramid
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))
    # Pyramid
    for i in range(2, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

n = int(input("Enter the number of rows: "))
hourglass(n)
