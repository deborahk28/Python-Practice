n = input("Enter the start number: ")
p = input("Enter the end number: ")

try:
    n = float(n)
    p = float(p)
    
    if n.is_integer() and p.is_integer():
        n = int(n)
        p = int(p)
        print("The integers from", n, "to", p, "are:")
        for i in range(n, p + 1):
            print(i)
    else:
        print("Input is not an integer.")
except ValueError:
    print("Input is not a number.")
