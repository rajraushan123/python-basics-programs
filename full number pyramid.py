def full_number_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

n = int(input("Enter the number of rows: "))
full_number_pyramid(n)
