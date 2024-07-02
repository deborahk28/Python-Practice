num = int(input("Enter the number of rows: "))

# Loop through each row in reverse order
for i in range(1,num+1):
    # Print asterisks for each row
    for j in range(1,(num+1)-i):
        print("*", end=" ")
    print()  # Move to the next line after printing each row
