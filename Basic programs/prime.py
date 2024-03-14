print("Program for checking if the number is prime or not")
n = int(input("Enter the number: "))

if n <= 1:
    print("Enter the number greater than 1")
else:
    is_prime = True  # Assume n is prime until proven otherwise
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False  # If n is divisible by any number in this range, it's not prime
            break  # No need to continue checking once a factor is found
    
    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")
