balance = 1000  # Starting balance

print("Welcome to Simple Bank!")
print("Your starting balance is:", balance)

# Deposit
deposit = int(input("Enter amount to deposit: "))
balance += deposit
print("New balance after deposit:", balance)

# Withdraw
withdraw = int(input("Enter amount to withdraw: "))
if withdraw <= balance:
    balance -= withdraw
    print("New balance after withdrawal:", balance)
else:
    print("Insufficient balance!")

# Final balance
print("Final balance:", balance)

