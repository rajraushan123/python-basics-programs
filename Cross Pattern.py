def cross_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if i == j or i + j == rows - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

n = int(input("Enter the number of rows: "))
cross_pattern(n)
