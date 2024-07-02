"""Print a pattern like this 
           A 
          A B 
         A B C 
        A B C D 
       A B C D E 

Use input elements method"""

n = int(input("enter the number of rows"))
alpha = 65
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end = " ")
    for j in range(0,i+1):
        print(chr(alpha), end= " ")
        alpha = alpha + 1
    alpha = 65
    print()