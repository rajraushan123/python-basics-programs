def hollow_rhombus(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print(' ' * (rows - i - 1) + '*' * rows)
        else:
            print(' ' * (rows - i - 1) + '*' + ' ' * (rows - 2) + '*')

n = int(input("Enter the number of rows: "))
hollow_rhombus(n)
