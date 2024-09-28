def butterfly_pattern(rows):
    # Upper part of butterfly
    for i in range(1, rows + 1):
        print('*' * i + ' ' * (2 * (rows - i)) + '*' * i)
    # Lower part of butterfly
    for i in range(rows, 0, -1):
        print('*' * i + ' ' * (2 * (rows - i)) + '*' * i)

n = int(input("Enter the number of rows: "))
butterfly_pattern(n)
