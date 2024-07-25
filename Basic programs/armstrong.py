#write a program to find if a number is armstrong number or not
def is_armstrong(number):
    # Convert number to string to easily iterate through digits
    digits = str(number)
    num_digits = len(digits)  # Number of digits
    
    # Calculate the sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Input from user
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
