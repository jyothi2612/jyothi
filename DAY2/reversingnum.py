# Get input from user
num = int(input("Enter a number: "))

# Initialize reversed number
reversed_num = 0

# Use while loop to reverse the number
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

# Print the result
print("Reversed number:",reversed_num)