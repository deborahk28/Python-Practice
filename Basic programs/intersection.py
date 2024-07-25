#write a program to find the intersection of 2 arrays
def intersection_of_arrays(arr1, arr2):
    # Convert lists to sets
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Find intersection
    intersection = set1 & set2
    
    return list(intersection)

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

print("Intersection:", intersection_of_arrays(array1, array2))
