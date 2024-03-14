print("Program for checking if the number is rational number or not")
n = int(input("Enter the numerator: "))
p = int(input("Enter the denominator: "))

if p == 0:
    print("Denominator cannot be zero. Number is undefined.")
else:
    q = n / p
    decimal_part = q - int(q)  # Extract the decimal part of the quotient

    # Check if the decimal part is zero (indicating that the number is rational)
    if decimal_part == 0:
        print("Number is rational")
    else:
        print("Number is irrational")
