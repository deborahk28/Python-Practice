def vowels_consonant_count():
    # Input the string from the user
    mystring = input("Enter the string: ").lower()
    
    # Define vowels
    vowels = "aeiou"
    
    # Initialize counters for vowels and consonants
    count_vowels = 0
    count_consonants = 0
    
    # Iterate through each character in the string
    for char in mystring:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                count_vowels += 1
            else:
                count_consonants += 1
    
    # Print the counts
    print(f"Number of vowels: {count_vowels}")
    print(f"Number of consonants: {count_consonants}")

# Call the function
vowels_consonant_count()
