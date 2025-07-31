# Get input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Use while loop to find GCD
while b != 0:
    a, b = b, a % b

# Print the result
print("GCDis:",a)