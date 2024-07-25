# Program to find the Fibonacci series up to a certain number of terms

nterms = int(input("Enter the number of terms: "))

# Initial values
n1, n2 = 0, 1
count = 0

# Handle cases where the number of terms is less than or equal to 0
if nterms <= 0:
    print("Enter a number of terms greater than 0")
# Handle the special case where the number of terms is 1
elif nterms == 1:
    print(n1)
# Compute and print the Fibonacci series
else:
    while count < nterms:
        print(n1)
        nth = n1 + n2  # Compute the next term
        # Update the values
        n1, n2 = n2, nth
        count += 1
