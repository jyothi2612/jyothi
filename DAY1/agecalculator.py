from datetime import date

# Get user input
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day: "))

# Get today's date
today = date.today()
birthdate = date(year, month, day)

# Calculate age
age = today.year - birthdate.year

# Adjust if birthday hasn't happened yet this year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

print("You are", age, "years old.")
