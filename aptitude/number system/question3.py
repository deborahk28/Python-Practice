#sum of 3 consecutive odd nums is 21. find the 3 numbers
# Initialize the first odd number
first_odd = 1

# Loop through all possible first odd numbers
while first_odd <= 21:
    # Check if the next two numbers are odd and their sum is 21
    if (first_odd % 2 != 0) and ((first_odd + 2) % 2 != 0) and ((first_odd + (first_odd + 2) + (first_odd + 4)) == 21):
        print("The three consecutive odd numbers whose sum is 21 are:", first_odd, first_odd + 2, first_odd + 4)
        break
    # Increment to the next possible first odd number
    first_odd += 2

#tracing:
#step 1: n=1,
# step 2: check the while condition n<=21 (1 is less than 21) go to while block
# step 3: check if condition if(n%2!=0) and if((n+2)%2!=0) and ((n+ (n+2) + (n+4))==21)
#[explain: 1%2!=0(no)] go to step 6
# step 4: print 
# step 6:Break the loop and goto step 7
# step 7:  n=n+2(1=1+2 i.e 3(n=3)) go to step 1 and repeat all steps
