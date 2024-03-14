print("Program for checking if the number is perfecr number or not")
n = int(input("Enter the number: "))

if n <= 0:
    print("Enter the number greater than 0")
else:
   divisor_sum = sum(i for i in range(1, n) if n % i == 0)
   if(divisor_sum==n):
       print(n,"is a pefect number")
   else:
       print(n,"not a perfect number")

   