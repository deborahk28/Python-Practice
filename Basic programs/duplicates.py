def find_duplicates(arr):
    print("Find duplicates in the array")
    
    duplicates = []
    seen = set()
    
    for i in arr:
        if i in seen:
            if i not in duplicates:
                duplicates.append(i)
        else:
            seen.add(i)
    
    return duplicates

# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Initialize an empty array
arr = []

# Check if size is zero
if size == 0:
    print("Size cannot be zero")
else:
    # Prompt the user to input the elements of the array
    for i in range(size):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    
    # Print the array
    print("The array is:", arr)

    # Find and print duplicates
    duplicates = find_duplicates(arr)
    if duplicates:
        print("Duplicates in the array are:", duplicates)
    else:
        print("No duplicates found in the array.")
