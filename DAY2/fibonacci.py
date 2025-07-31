# Get number of terms from user
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1

# Print the Fibonacci series
print("Fibonacci series:")
for i in range(n):
    print(a, end="")
    a,b=b,a+b
    print()
