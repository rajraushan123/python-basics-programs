def inverted_left_triangle(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

n = int(input("Enter the number of rows: "))
inverted_left_triangle(n)
