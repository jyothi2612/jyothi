# Get input from user
text = input("Enter a string: ")

# Initialize vowel count
vowel_count = 0

# Define vowels (you can include uppercase if needed)
vowels = "aeiouAEIOU"

# Use for loop to count vowels
for char in text:
    if char in vowels:
        vowel_count += 1

# Print the result
print("Number of vowels:",vowel_count)