def find_second_largest(arr):
    # Handle edge cases
    if len(arr) < 2:
        return None  # Not enough elements to find the second largest
    
    # Initialize the largest and second largest
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            # Update second largest before updating largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Update second largest
            second_largest = num

    # If second largest is still negative infinity, it means there was no valid second largest
    if second_largest == float('-inf'):
        return None

    return second_largest

# Example usage
a = [23, 45, 67, 83, 1, 2, 45, 67]
second_largest = find_second_largest(a)

if second_largest is not None:
    print(f"The second largest element is: {second_largest}")
else:
    print("The array does not have a second largest element.")
