def hollow_diamond(rows):
    # Upper hollow pyramid
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))
    # Lower hollow inverted pyramid
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))

n = int(input("Enter the number of rows: "))
hollow_diamond(n)
