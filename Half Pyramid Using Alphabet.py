def alphabet_half_pyramid(rows):
    alphabet = 65  # ASCII value of 'A'
    for i in range(1, rows + 1):
        print((chr(alphabet) + ' ') * i)
        alphabet += 1

n = int(input("Enter the number of rows: "))
alphabet_half_pyramid(n)
