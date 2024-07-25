#write a program to print all the permutations of a string

def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  # Swap
            permute(s, l + 1, r)  # Recurse
            s[l], s[i] = s[i], s[l]  # Swap back

# Input from user
string = input("Enter a string: ")

# Convert string to list of characters
char_list = list(string)

# Print permutations
print("Permutations are:")
permute(char_list, 0, len(char_list) - 1)
