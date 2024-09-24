# Function to print pyramid pattern
def print_pyramid(rows):
    for i in range(rows):
        # Printing spaces
        print(' ' * (rows - i - 1), end='')
        # Printing stars
        print('*' * (2 * i + 1))

# Input number of rows
n = int(input("Enter the number of rows: "))

# Call function to print pyramid
print_pyramid(n)
