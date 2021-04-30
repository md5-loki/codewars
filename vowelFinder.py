def vowel_indices(word):
    amount_vowels = [] # Create array to store the vowel positions
    
    for position, vowel in enumerate(word): # Loop thru the word to find vowels and positions
        if vowel in "AEIOUYaeiouy": # Check if the word contains a vowel
            amount_vowels.append(position + 1) # Add 1 to simulate array starting from 1 instead of 0
    return amount_vowels
            
print(vowel_indices("UNDISARMED"))
