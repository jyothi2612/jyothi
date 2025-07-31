# Get input from user
num = int(input("Enter a number: "))

# Initialize sum
sum_of_digits = 0

# Use while loop to extract and add digits
while num > 0:
    digit = num % 10          # Get the last digit
    sum_of_digits += digit    # Add it to the sum
    num = num // 10           # Remove the last digit

# Print the result
print("Sum of digits:",sum_of_digits)