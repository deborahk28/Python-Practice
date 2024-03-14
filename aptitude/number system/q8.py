#1397 x 1397 = ?
# multiplicand=int(input("Enter the multiplicand"))
# multiplier=int(input("Enter the multiplier"))

# if multiplicand==multiplier:

# Take input for the first number
num1 = int(input("Enter the first number: "))

# Take input for the operation (e.g., '-')
operation = input("Enter the operation (+, -, *, /, **): ")

# Take input for the second number
num2 = int(input("Enter the second number: "))

# Evaluate the expression
if operation == '**':
    result = num1 ** num2
else:
    result = eval(f"{num1} {operation} {num2}")

# Print the result
print("Result:", result)
