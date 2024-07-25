# Function to calculate the sum of digits of a number
def sum_of_digits(num):
    total = 0
    while num > 0:
        # Extract the last digit and add it to the total
        total += num % 10
        # Remove the last digit
        num //= 10
    return total

# Input: Number
num = int(input("Enter the number: "))

# Function call and output
print("Sum of digits:", sum_of_digits(num))
