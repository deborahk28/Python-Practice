print("Program for checking if the number is twin prime or not")
n = int(input("Enter the 1st number: "))
p = int(input("Enter the 2nd number: "))

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Check if both numbers are prime and their difference is 2
if is_prime(n) and is_prime(p) and abs(n - p) == 2:
    print("Twin prime")
else:
    print("Not twin prime")
