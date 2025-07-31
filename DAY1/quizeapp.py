score = 0

# Question 1
print("1. What is the capital of France?")
print("A. Paris\nB. London\nC. Rome\nD. Berlin")
ans = input("Your answer: ").upper()
if ans == "A":
    score += 1

# Question 2
print("\n2. What is 2 + 2?")
print("A. 3\nB. 4\nC. 5\nD. 6")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

# Question 3
print("\n3. What color is the sky?")
print("A. Blue\nB. Green\nC. Red\nD. Yellow")
ans = input("Your answer: ").upper()
if ans == "A":
    score += 1

# Question 4
print("\n4. What is the largest planet?")
print("A. Earth\nB. Mars\nC. Jupiter\nD. Venus")
ans = input("Your answer: ").upper()
if ans == "C":
    score += 1

# Question 5
print("\n5. Which animal barks?")
print("A. Cat\nB. Dog\nC. Cow\nD. Bird")
ans = input("Your answer: ").upper()
if ans == "B":
    score += 1

# Final Score
print("\nYou got", score, "out of 5 correct.")
