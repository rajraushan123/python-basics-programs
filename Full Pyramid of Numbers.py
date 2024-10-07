def number_full_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        print((str(i) + ' ') * i)

n = int(input("Enter the number of rows: "))
number_full_pyramid(n)
