# ==========================================
# Python Loops Tutorial
# ==========================================

# 1. Basic List/Array Interation
# This is the most common way to loop in Python.
print("--- 1. Basic List Iteration ---")
fruits = ["Apple", "Banana", "Cherry", "Date"]
for fruit in fruits:
    print(f"Fruit in list: {fruit}")

# 2. range() - Numeric Sequences
# range(start, stop, step)
# Start: inclusive | Stop: exclusive | Step: increment
print("\n--- 2. range(start, stop, step) ---")
print("Numbers from 1 to 5 (exclusive of 5):")
for i in range(1, 5):
    print(i, end=" ")  # 1, 2, 3, 4

print("\n\nNumbers from 10 to 20 with step 2:")
for i in range(10, 22, 2):
    print(i, end=" ")  # 10, 12, 14, 16, 18, 20
print()

# 3. enumerate() - Index and Value
# Use this when you need the position (index) of the item.
print("\n--- 3. enumerate() ---")
students = ["Amit", "Sneha", "Rahul", "Priya"]
for index, name in enumerate(students):
    print(f"Student #{index + 1}: {name}")

# 4. Dictionary Iteration
# You can iterate over keys, values, or both (items).
print("\n--- 4. Dictionary Iteration ---")
person = {
    "name": "Shubhdeep",
    "role": "Developer",
    "language": "Python",
    "city": "Mumbai",
}

# 4a. Iterating over Key-Value pairs (Recommended)
print("Key-Value Pairs:")
for key, value in person.items():
    print(f"  {key.title()}: {value}")

# 4b. Iterating over only Values
print("\nOnly Values:")
for value in person.values():
    print(f"  {value}")

# 5. zip() - Multiple Sequences
# Parallel iteration through two or more lists.
print("\n--- 5. zip() parallel iteration ---")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
subjects = ["Math", "Science", "History"]

for name, score, subject in zip(names, scores, subjects):
    print(f"{name} scored {score} in {subject}")

# 6. while Loops
# Continues as long as the condition is True.
print("\n--- 6. while loop (Countdown) ---")
timer = 3
while timer > 0:
    print(f"  T-minus {timer}...")
    timer -= 1
print("  Blast off! 🚀")

# 7. Loop Control: break and continue
# break stops the loop completely.
# continue skips to the next iteration.
print("\n--- 7. Loop Control: break & continue ---")
for num in range(1, 11):
    if num == 3:
        print("  (Skipping 3 using continue)")
        continue
    if num == 7:
        print("  (Breaking at 7 using break)")
        break
    print(f"  Number: {num}")
