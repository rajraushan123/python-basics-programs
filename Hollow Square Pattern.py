def hollow_square(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print('*' * rows)
        else:
            print('*' + ' ' * (rows - 2) + '*')

n = int(input("Enter the number of rows: "))
hollow_square(n)
