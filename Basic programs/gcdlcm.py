def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Input: Two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD and LCM
gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)

# Print the results
print(f"The GCD of {num1} and {num2} is: {gcd_result}")
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
