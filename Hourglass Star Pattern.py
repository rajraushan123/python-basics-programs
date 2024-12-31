def hourglass_star(rows):
    # Upper half of hourglass
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))
    # Lower half of hourglass
    for i in range(2, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

n = int(input("Enter the number of rows: "))
hourglass_star(n)
