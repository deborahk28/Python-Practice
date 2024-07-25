n = input("Enter the number or string to find the palindrome of it: ")

original_num = str(n)
reversed_num = n[::-1]
if original_num == reversed_num:
    print("Palindrome") 
else:
    print("not palindrome")   
