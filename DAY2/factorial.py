# Get input from user
num = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Use for loop to calculate factorial
for i in range(1, num + 1):
    factorial *= i

# Print the result
print("Factorial of", num, "is",factorial)