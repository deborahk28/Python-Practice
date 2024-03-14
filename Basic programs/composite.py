print("Program for checking if the number is composite or not")
n = int(input("Enter the number: "))

if n <= 1:
    print("Enter the number greater than 1")
else:
    is_composite = False 
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_composite = True  # If n is divisible by any number in this range, it's not prime
            break  # No need to continue checking once a factor is found
    
    if is_composite:
        print(n, "is a composite number")
    else:
        print(n, "is  a prime number")
