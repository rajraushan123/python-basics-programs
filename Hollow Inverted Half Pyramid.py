def hollow_inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        if i == rows or i == 1:
            print('*' * i)
        else:
            print('*' + ' ' * (i - 2) + '*')

n = int(input("Enter the number of rows: "))
hollow_inverted_half_pyramid(n)
