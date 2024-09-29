def diagonal_star(rows):
    for i in range(1, rows + 1):
        print(' ' * (i - 1) + '*')

n = int(input("Enter the number of rows: "))
diagonal_star(n)
