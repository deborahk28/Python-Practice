#write a program to merge 2 sorted arrays
arr1 = [45,61,20,8,3]
arr2 = [67,72,90,56,1]

a_sort = sorted(arr1)
b_sort = sorted(arr2)

merge_arr = sorted(a_sort + b_sort)

print(merge_arr)