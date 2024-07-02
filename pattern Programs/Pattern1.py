"""Print a pattern like this 
*
* *
* * *
* * * *
* * * * * 
Use input elements method"""

num = int(input("enter the number of rows"))
for i in range(0,num+1):
    for j in range(0,i+1):
        print("*" , end=" ")
    print()