def hollow_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        if i == rows:
            print('*' * (2 * i - 1))
        else:
            print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))

n = int(input("Enter the number of rows: "))
hollow_inverted_pyramid(n)
