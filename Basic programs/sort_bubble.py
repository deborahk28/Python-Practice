#write a program to sort the array elements using bubble sort
arr = [67,87,56,43,23,1,89,54]

n = len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            print(arr)
            
