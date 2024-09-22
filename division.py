# Function to divide two numbers
def divide_numbers(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = divide_numbers(num1, num2)
print(f"The result of {num1} / {num2} is: {result}")
