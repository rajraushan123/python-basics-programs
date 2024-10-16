def hollow_right_triangle(rows):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print('*' * i)
        else:
            print('*' + ' ' * (i - 2) + '*')

n = int(input("Enter the number of rows: "))
hollow_right_triangle(n)
