
# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# Get input from the user
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Perform operations
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
