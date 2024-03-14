print("Program to print natural numbers")
n=int(input("enter the starting number"))
p=int(input("enter the end number"))

if(n==0 or p==0):
        print("Zero(0) is not a natural number")
else:
    print("The natural numbers from",n ," to",p, "are")
    for i in range(n, p + 1):
        print(i)