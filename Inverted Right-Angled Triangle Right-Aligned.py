def inverted_right_triangle(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * i)

n = int(input("Enter the number of rows: "))
inverted_right_triangle(n)
