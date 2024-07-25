# Swap 2 numbers without temp using arithmetic operations
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

a = a + b  # i.e. a = A + B
b = a - b  # i.e. b = (A + B) - B => A
a = a - b  # i.e. a = (A + B) - A => B

print("After swapping: a =", a, ", b =", b)

# Swap 2 strings without using a temporary variable
# a = input("Enter value of a: ")
# b = input("Enter value of b: ")

# a = a + b  # Combine both strings
# b = a[:len(a) - len(b)]  # Extract the original value of 'a'
# a = a[len(b):]  # Extract the original value of 'b'

# print("After swapping: a =", a, ", b =", b)

