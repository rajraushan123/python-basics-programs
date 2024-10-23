def left_aligned_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

n = int(input("Enter the number of rows: "))
left_aligned_triangle(n)
