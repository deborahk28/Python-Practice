#write a program to check if 2 strings are anagrams
#anagrams meaning : same letters are used to form 2 different words

my_string = input("enter 1st string: ").lower()
my_string2 = input("enter 2nd string: ").lower()

length1 = len(my_string)
length2 = len(my_string2)

if(length1!=length2):
    print("size of the strings has to be same")
else:
    sort1 = sorted(my_string)
    sort2 = sorted(my_string2)
    if(sort1==sort2):
        print("Anagrams")
    else:
        print("not anagrams")



                
    