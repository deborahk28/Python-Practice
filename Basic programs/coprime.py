def are_coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False  # If a common divisor is found, numbers are not coprime
    return True  # If no common divisor found, numbers are coprime

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if are_coprime(num1, num2):
    print(num1, "and", num2, "are coprime")
else:
    print(num1, "and", num2, "are not coprime")
