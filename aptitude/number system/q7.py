#What least number must be added to 1056, so that the sum is completely divisible by 23 ?
num1=int(input("enter the number 1"))
num2=int(input("enter the number 2"))

result1=int(num1%num2)

result2= int(num2-result1)
print("least number must be added to 1056, so that the sum is completely divisible by 23 is :",result2)