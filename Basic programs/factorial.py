#write a program to find factorial of a number using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Input: Number
num = int(input("Enter a number to find its factorial: "))

# Function call and output
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
