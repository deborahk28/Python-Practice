"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 """

n = 5  # Number of rows

# Loop through each row
num = 1
for i in range(n):
    # Print numbers for each row
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()  # Move to the next line after printing each row
