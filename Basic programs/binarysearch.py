def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        mid_value = arr[mid]  # Value at the middle index

        if mid_value == target:
            return mid  # Target found
        elif mid_value < target:
            low = mid + 1  # Target is in the upper half
        else:
            high = mid - 1  # Target is in the lower half

    return -1  # Target not found

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
