def binary_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        for j in range(1, 2 * i):
            print(j % 2, end=' ')
        print()

n = int(input("Enter the number of rows: "))
binary_pyramid(n)
