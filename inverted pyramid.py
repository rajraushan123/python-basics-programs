# Function to print inverted pyramid pattern
def print_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        # Printing spaces
        print(' ' * (rows - i), end='')
        # Printing stars
        print('*' * (2 * i - 1))

# Input number of rows
n = int(input("Enter the number of rows: "))

# Call function to print inverted pyramid
print_inverted_pyramid(n)
